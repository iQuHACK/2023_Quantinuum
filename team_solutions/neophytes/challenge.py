import time

from scipy.optimize import approx_fprime
from typing import Callable, List, Tuple
from sympy.core.symbol import Symbol
from pytket.circuit import fresh_symbol

import networkx as nx
import numpy as np
from pytket import Circuit, Qubit
from pytket.backends.backend import Backend
from pytket.backends.backendresult import BackendResult
from pytket.extensions.qiskit import AerBackend
from pytket.passes.auto_rebase import auto_rebase_pass

from pytket.passes import DecomposeBoxes, RemoveRedundancies
from pytket.pauli import Pauli, QubitPauliString
from pytket.utils import QubitPauliOperator, gen_term_sequence_circuit

from maxcut_plotting import plot_maxcut_results

max_cut_graph_edges = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (4, 6)]
expected_results = [(0, 1, 0, 0, 1, 0, 0), (1, 0, 1, 1, 0, 1, 1)]
n_nodes = 7


def main():
    cost_angle = 1.0
    cost_ham_qpo = qaoa_graph_to_cost_hamiltonian(max_cut_graph_edges, cost_angle)
    print(cost_ham_qpo)

    max_cut_graph = nx.Graph()
    max_cut_graph.add_edges_from(max_cut_graph_edges)
    nx.draw(max_cut_graph, labels={node: node for node in max_cut_graph.nodes()})
    backend = AerBackend()

    shots = 5000
    iterations = 100
    seed = 12345
    start = time.time()
    res_neophytes = qaoa_calculate(
        backend,
        backend.default_compilation_pass(2).apply,
        shots=shots,
        iterations=iterations,
        seed=seed
    )

    end = time.time()
    print(f"Total time for {iterations} iterations (ms): {(end - start) * 1000}")

    plot_maxcut_results(
        res_neophytes,
        6,
        "neophytes.png"
    )


def qaoa_graph_to_cost_hamiltonian(
        edges: List[Tuple[int, int]], cost_angle: float
) -> QubitPauliOperator:
    qpo_dict = {QubitPauliString(): len(edges) * 0.5 * cost_angle}
    for e in edges:
        term_string = QubitPauliString([Qubit(e[0]), Qubit(e[1])], [Pauli.Z, Pauli.Z])
        qpo_dict[term_string] = -0.5 * cost_angle
    return QubitPauliOperator(qpo_dict)


def qaoa_calculate(
        backend: Backend,
        compiler_pass: Callable[[Circuit], bool],
        shots: int = 5000,
        iterations: int = 100,
        seed: int = 12345
) -> BackendResult:

    cost_syms, mixer_syms, sym_circ = qaoa_max_cut_circuit_symbolic(
        edges=max_cut_graph_edges,
        n_nodes=n_nodes,
        n=3,
        backend=backend
    )

    # find the parameters for the highest energy
    best_mixer, best_cost = qaoa_optimise_energy(
        backend=backend,
        cost_syms=cost_syms,
        mixer_syms=mixer_syms,
        sym_circ=sym_circ,
        iterations=iterations,
        n=3,
        shots=shots,
        seed=seed
    )

    # update the symbolic circuit for the final time
    my_qaoa_circuit = qaoa_max_cut_circuit_fill(
        cost_angles=best_cost,
        mixer_angles=best_mixer,
        cost_syms=cost_syms,
        mixer_syms=mixer_syms,
        sym_circ=sym_circ
    )

    my_qaoa_circuit.measure_all()

    handle = backend.process_circuit(my_qaoa_circuit, shots, seed=seed)

    result = backend.get_result(handle)

    return result


def qaoa_optimise_energy(
        backend: Backend,
        cost_syms: List[Symbol],
        mixer_syms: List[Symbol],
        sym_circ: Circuit,
        iterations: int = 100,
        n: int = 3,
        shots: int = 5000,
        seed: int = 12345,
):
    rng = np.random.default_rng(seed)
    print(f"Optimization method: Gradient Ascent")

    guess = rng.uniform(0, 1, 2 * n)

    (
        best_guess_cost_angles,
        best_guess_mixer_angles,
    ) = gradient_ascent_finite_difference_approx(
        cost_syms=cost_syms,
        mixer_syms=mixer_syms,
        sym_circ=sym_circ,
        iterations=iterations,
        shots=shots,
        n=n,
        guess=guess,
        seed=seed,
        backend=backend,
    )

    return best_guess_mixer_angles, best_guess_cost_angles


def gradient_ascent_finite_difference_approx(
        iterations: int,
        shots: int,
        n: int,
        guess,
        seed: int,
        backend: Backend,
        cost_syms: List[Symbol],
        mixer_syms: List[Symbol],
        sym_circ: Circuit,
        decay_rate: float = 1e-2,
        step_size: float = 1e-2,
        finite_diff: float = 1.5e-3,
):
    best_energy = 0
    diff = 0
    for i in range(iterations):
        print(f"Iteration: {i}")
        fprime = approx_fprime(
            guess,
            my_qaoa_instance,
            finite_diff,
            backend,
            cost_syms,
            mixer_syms,
            sym_circ,
            seed,
            shots
        )

        diff = decay_rate * diff + step_size * fprime
        guess += diff
        guess = [x % 1 for x in guess]
        guess_mixer_angles = guess[:n]
        guess_cost_angles = guess[n:]

        qaoa_energy = qaoa_instance_simple(
            cost_syms=cost_syms,
            mixer_syms=mixer_syms,
            sym_circ=sym_circ,
            backend=backend,
            guess_mixer_angles=guess_mixer_angles,
            guess_cost_angles=guess_cost_angles,
            seed=seed,
            shots=shots,
        )

        if qaoa_energy > best_energy:
            best_energy = qaoa_energy
        print(f"energy found: {qaoa_energy} - best: {best_energy}")
    best_guess_mixer_angles = guess[:n]
    best_guess_cost_angles = guess[n:]
    print(f"Best Cost Angles: {best_guess_cost_angles}")
    print(f"Best Mixer Angles: {best_guess_mixer_angles}")
    print(f"Energy: {qaoa_energy}")
    return best_guess_cost_angles, best_guess_mixer_angles


def my_qaoa_instance(
    angles,
    backend,
    cost_syms,
    mixer_syms,
    sym_circ,
    seed,
    shots
):
    n = len(angles) // 2
    guess_mixer_angles = angles[:n]
    guess_cost_angles = angles[n:]
    return qaoa_instance_simple(
        backend=backend,
        cost_syms=cost_syms,
        mixer_syms=mixer_syms,
        sym_circ=sym_circ,
        guess_mixer_angles=guess_mixer_angles,
        guess_cost_angles=guess_cost_angles,
        seed=seed,
        shots=shots,
    )


def qaoa_instance_simple(
        backend: Backend,
        cost_syms: List[Symbol],
        mixer_syms: List[Symbol],
        sym_circ: Circuit,
        guess_mixer_angles: np.array,
        guess_cost_angles: np.array,
        seed: int,
        shots: int = 5000,
) -> float:

    # step 1: get state guess
    my_prep_circuit = qaoa_max_cut_circuit_fill(
        mixer_angles=guess_mixer_angles,
        cost_angles=guess_cost_angles,
        cost_syms=cost_syms,
        mixer_syms=mixer_syms,
        sym_circ=sym_circ
    )
    measured_circ = my_prep_circuit.copy().measure_all()
    res = backend.run_circuit(measured_circ, shots, seed=seed)

    return max_cut_energy(max_cut_graph_edges, res)


def qaoa_max_cut_circuit(
        edges: List[Tuple[int, int]],
        n_nodes: int,
        mixer_angles: List[float],
        cost_angles: List[float],
) -> Circuit:
    assert len(mixer_angles) == len(cost_angles)

    # initial state
    qaoa_circuit = qaoa_initial_circuit(n_nodes)

    # add cost and mixer terms to state
    for cost, mixer in zip(cost_angles, mixer_angles):
        cost_ham = qaoa_graph_to_cost_hamiltonian(edges, cost)
        mixer_ham = QubitPauliOperator(
            {QubitPauliString([Qubit(i)], [Pauli.X]): mixer for i in range(n_nodes)}
        )
        qaoa_circuit.append(gen_term_sequence_circuit(cost_ham, Circuit(n_nodes)))
        qaoa_circuit.append(gen_term_sequence_circuit(mixer_ham, Circuit(n_nodes)))

    DecomposeBoxes().apply(qaoa_circuit)
    return qaoa_circuit


def max_cut_energy(edges: List[Tuple[int, int]], results: BackendResult) -> float:
    energy = 0.0
    dist = results.get_distribution()
    for i, j in edges:
        energy += sum((meas[i] ^ meas[j]) * prob for meas, prob in dist.items())

    return energy


def qaoa_initial_circuit(n_qubits: int) -> Circuit:
    c = Circuit(n_qubits)
    for i in range(n_qubits):
        c.H(i)
    return c

# CHALLENGE 4
def qaoa_max_cut_circuit_symbolic(
        edges: List[Tuple[int, int]],
        n_nodes: int,
        n: int,
        backend: Backend
) -> tuple[List[Symbol], List[Symbol], Circuit]:

    qaoa_circuit_sym = qaoa_initial_circuit(n_nodes)
    cost_syms = [fresh_symbol("cost") for _ in range(n)]
    mixer_syms = [fresh_symbol("mixer") for _ in range(n)]
    for idx in range(n):
        cost_ham_sym = qaoa_graph_to_cost_hamiltonian(edges, cost_syms[idx])
        mixer_ham_sym = QubitPauliOperator(
            {QubitPauliString([Qubit(i)], [Pauli.X]): mixer_syms[idx] for i in range(n_nodes)})
        qaoa_circuit_sym.append(gen_term_sequence_circuit(
            cost_ham_sym, Circuit(n_nodes)))
        qaoa_circuit_sym.append(gen_term_sequence_circuit(
            mixer_ham_sym, Circuit(n_nodes)))

    DecomposeBoxes().apply(qaoa_circuit_sym)

    gate_set = backend.backend_info.gate_set
    auto_rebaser = auto_rebase_pass(gateset=gate_set)
    auto_rebaser.apply(qaoa_circuit_sym)

    RemoveRedundancies().apply(qaoa_circuit_sym)

    return cost_syms, mixer_syms, qaoa_circuit_sym


def qaoa_max_cut_circuit_fill(
        cost_angles: List[float],
        mixer_angles: List[float],
        cost_syms: List[Symbol],
        mixer_syms: List[Symbol],
        sym_circ: Circuit
):
    circ = sym_circ.copy()
    sym_args = {k: v for k, v in zip(cost_syms, cost_angles)}
    sym_args.update({k: v for k, v in zip(mixer_syms, mixer_angles)})
    circ.symbol_substitution(sym_args)

    return circ


if __name__ == "__main__":
    main()
