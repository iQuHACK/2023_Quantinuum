import time
from typing import Callable, List, Tuple
from sympy.core.symbol import Symbol
from pytket.circuit import fresh_symbol

import networkx as nx
import numpy as np
from pytket import Circuit, Qubit
from pytket.backends.backend import Backend
from pytket.backends.backendresult import BackendResult
from pytket.extensions.qiskit import AerBackend
from pytket.extensions.quantinuum import QuantinuumBackend

from pytket.passes import DecomposeBoxes
from pytket.pauli import Pauli, QubitPauliString
from pytket.utils import QubitPauliOperator, gen_term_sequence_circuit

from maxcut_plotting import plot_maxcut_results

from qiskit import IBMQ


from pytket.extensions.qiskit import IBMQEmulatorBackend


def max_cut_energy(edges: List[Tuple[int, int]], results: BackendResult) -> float:
    energy = 0.0
    dist = results.get_distribution()
    for i, j in edges:
        energy += sum((meas[i] ^ meas[j]) * prob for meas, prob in dist.items())

    return energy


def qaoa_graph_to_cost_hamiltonian(edges: List[Tuple[int, int]], cost_angle: float) -> QubitPauliOperator:
    qpo_dict = {QubitPauliString(): len(edges) * 0.5 * cost_angle}
    for e in edges:
        term_string = QubitPauliString(
            [Qubit(e[0]), Qubit(e[1])], [Pauli.Z, Pauli.Z])
        qpo_dict[term_string] = -0.5 * cost_angle
    return QubitPauliOperator(qpo_dict)


def qaoa_initial_circuit(n_qubits: int) -> Circuit:
    c = Circuit(n_qubits)
    for i in range(n_qubits):
        c.H(i)
    return c


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
    # TODO
    qaoa_circuit_sym = backend.get_compiled_circuit(qaoa_circuit_sym)
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


def qaoa_instance_simple(
        backend: Backend,
        cost_syms: List[Symbol],
        mixer_syms: List[Symbol],
        sym_circ: Circuit,
        # compiler_pass: Callable[[Circuit], bool],
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
    # compiler_pass(measured_circ)
    res = backend.run_circuit(measured_circ, shots, seed=seed)

    return max_cut_energy(max_cut_graph_edges, res)


def qaoa_optimise_energy(
        # compiler_pass: Callable[[Circuit], bool],
        backend: Backend,
        cost_syms: List[Symbol],
        mixer_syms: List[Symbol],
        sym_circ: Circuit,
        iterations: int = 100,
        n: int = 3,
        shots: int = 5000,
        seed: int = 12345,
):
    highest_energy = 0
    best_guess_mixer_angles = [0 for i in range(n)]
    best_guess_cost_angles = [0 for i in range(n)]
    rng = np.random.default_rng(seed)
    # guess some angles (iterations)-times and try if they are better than the best angles found before

    for i in range(iterations):

        guess_mixer_angles = rng.uniform(0, 1, n)
        guess_cost_angles = rng.uniform(0, 1, n)

        qaoa_energy = qaoa_instance_simple(
            backend=backend,
            cost_syms=cost_syms,
            mixer_syms=mixer_syms,
            sym_circ=sym_circ,
            # compiler_pass=compiler_pass,
            guess_mixer_angles=guess_mixer_angles,
            guess_cost_angles=guess_cost_angles,
            seed=seed,
            shots=shots,
        )

        if qaoa_energy > highest_energy:
            print("new highest energy found: ", qaoa_energy)

            best_guess_mixer_angles = guess_mixer_angles
            best_guess_cost_angles = guess_cost_angles
            highest_energy = qaoa_energy

    print("highest energy: ", highest_energy)
    print("best guess mixer angles: ", best_guess_mixer_angles)
    print("best guess cost angles: ", best_guess_cost_angles)
    return best_guess_mixer_angles, best_guess_cost_angles


def qaoa_calculate(
        cost_syms: List[Symbol],
        mixer_syms: List[Symbol],
        sym_circ: Circuit,
        backend: Backend,
        # compiler_pass: Callable[[Circuit], bool],
        shots: int = 5000,
        iterations: int = 100,
        seed: int = 12345,
) -> float:

    # find the parameters for the highest energy
    best_mixer, best_cost = qaoa_optimise_energy(
        # compiler_pass,
        backend,
        cost_syms=cost_syms,
        mixer_syms=mixer_syms,
        sym_circ=sym_circ,
        iterations=iterations,
        n=3,
        shots=shots,
        seed=seed
    )

    # get the circuit with the final parameters of the optimisation:
    my_qaoa_circuit = qaoa_max_cut_circuit_fill(
        mixer_angles=best_mixer,
        cost_angles=best_cost,
        cost_syms=cost_syms,
        mixer_syms=mixer_syms,
        sym_circ=sym_circ
    )

    my_qaoa_circuit.measure_all()

    # compiler_pass(my_qaoa_circuit)
    handle = backend.process_circuit(my_qaoa_circuit, shots, seed=seed)

    result = backend.get_result(handle)

    return result


max_cut_graph_edges = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (4, 6)]
n_nodes_ = 7

max_cut_graph_ = nx.Graph()
max_cut_graph_.add_edges_from(max_cut_graph_edges)
# nx.draw(max_cut_graph_, labels={node: node for node in max_cut_graph_.nodes()})

expected_results = [(0, 1, 0, 0, 1, 0, 0), (1, 0, 1, 1, 0, 1, 1)]

cost_angle_ = 1.0
cost_ham_qpo_ = qaoa_graph_to_cost_hamiltonian(max_cut_graph_edges, cost_angle_)
print(cost_ham_qpo_)

# backend_ = AerBackend()
backend_ = QuantinuumBackend("H1-2SC")

# Create a symbolic circuit and collect the symbols
cost_syms_, mixer_syms_, sym_circ_ = qaoa_max_cut_circuit_symbolic(
    max_cut_graph_edges, n_nodes_, 3, backend_)
iters = 10

start = time.time()
res_ = qaoa_calculate(
    backend=backend_,
    cost_syms=cost_syms_,
    mixer_syms=mixer_syms_,
    sym_circ=sym_circ_,
    # compiler_pass=backend_.default_compilation_pass(2).apply,
    shots=5000,
    iterations=iters,
    seed=12345,
)

end = time.time()
print(f"Total time for {iters} iterations (ms): {(end - start) * 1000}")

# plot_maxcut_results(res_, 6)
