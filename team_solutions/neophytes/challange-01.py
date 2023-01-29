import networkx as nx

max_cut_graph_edges = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (4, 6)]
n_nodes = 7

max_cut_graph = nx.Graph()
max_cut_graph.add_edges_from(max_cut_graph_edges)
nx.draw(max_cut_graph, labels={node: node for node in max_cut_graph.nodes()})

expected_results = [(0, 1, 0, 0, 1, 0, 0), (1, 0, 1, 1, 0, 1, 1)]

from typing import List, Tuple, Callable
from pytket.utils import QubitPauliOperator
from pytket.pauli import QubitPauliString, Pauli
from pytket import Circuit, Qubit
import numpy as np

from scipy.optimize import approx_fprime, minimize


def qaoa_graph_to_cost_hamiltonian(
        edges: List[Tuple[int, int]], cost_angle: float
) -> QubitPauliOperator:
    qpo_dict = {QubitPauliString(): len(edges) * 0.5 * cost_angle}
    for e in edges:
        term_string = QubitPauliString([Qubit(e[0]), Qubit(e[1])], [Pauli.Z, Pauli.Z])
        qpo_dict[term_string] = -0.5 * cost_angle
    return QubitPauliOperator(qpo_dict)


cost_angle = 1.0
cost_ham_qpo = qaoa_graph_to_cost_hamiltonian(max_cut_graph_edges, cost_angle)
print(cost_ham_qpo)


def qaoa_initial_circuit(n_qubits: int) -> Circuit:
    c = Circuit(n_qubits)
    for i in range(n_qubits):
        c.H(i)
    return c


from pytket.utils import gen_term_sequence_circuit
from pytket.passes import DecomposeBoxes


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


from pytket.backends.backendresult import BackendResult


def max_cut_energy(edges: List[Tuple[int, int]], results: BackendResult) -> float:
    energy = 0.0
    dist = results.get_distribution()
    for i, j in edges:
        energy += sum((meas[i] ^ meas[j]) * prob for meas, prob in dist.items())

    return energy


from pytket.backends.backend import Backend

def my_qaoa_instance(angles,
                     backend,
                     compiler_pass,
                     seed,
                     shots):
    n = len(angles) // 2
    guess_mixer_angles = angles[:n]
    guess_cost_angles = angles[n:]
    return qaoa_instance_simple(
            backend,
            compiler_pass,
            guess_mixer_angles,
            guess_cost_angles,
            seed=seed,
            shots=shots,
        )

def qaoa_instance_simple(
        backend: Backend,
        compiler_pass: Callable[[Circuit], bool],
        guess_mixer_angles: np.array,
        guess_cost_angles: np.array,
        seed: int,
        shots: int = 5000,
) -> float:
    # step 1: get state guess
    my_prep_circuit = qaoa_max_cut_circuit(
        max_cut_graph_edges, n_nodes, guess_mixer_angles, guess_cost_angles
    )
    measured_circ = my_prep_circuit.copy().measure_all()
    compiler_pass(measured_circ)
    res = backend.run_circuit(measured_circ, shots, seed=seed)

    return max_cut_energy(max_cut_graph_edges, res)


def qaoa_optimise_energy(
        compiler_pass: Callable[[Circuit], bool],
        backend: Backend,
        iterations: int = 100,
        n: int = 3,
        shots: int = 5000,
        seed: int = 12345,
):
    # highest_energy = 0
    # best_guess_mixer_angles = [0 for i in range(n)]
    # best_guess_cost_angles = [0 for i in range(n)]
    rng = np.random.default_rng(seed)
    # guess some angles (iterations)-times and try if they are better than the best angles found before

    guess = rng.uniform(0, 1, 2 * n)
    best_energy = 0
    step_size = 0.01
    # result = minimize(my_qaoa_instance,
    #                   guess, args=(
    #                        backend,
    #                        compiler_pass,
    #                        seed,
    #                        shots),
    #                   method="Nelder-Mead"
    #                        )
    diff = 0
    decay_rate = 0.01
    for i in range(iterations):
        print(f"Iteration: {i}")
        fprime = approx_fprime(guess,
                               my_qaoa_instance,
                               1.5e-3,
                               backend,
                               compiler_pass,
                               seed,
                               shots
                               )

        print(f"fprime shape: {fprime.shape}")
        print(f"fprime: {fprime}")
        print(f"guess: {guess}")
        diff = decay_rate * diff + step_size * fprime
        print(f"diff: {diff}")
        print(f"norm fprime: {np.linalg.norm(fprime)}")
        if np.linalg.norm(fprime) < 1e-4:
            break
        guess += diff
        guess = [x % 1 for x in guess]
        guess_mixer_angles = guess[:n]
        guess_cost_angles = guess[n:]
        qaoa_energy = qaoa_instance_simple(
            backend,
            compiler_pass,
            guess_mixer_angles,
            guess_cost_angles,
            seed=seed,
            shots=shots,
        )

        print("energy found: ", qaoa_energy)
        if qaoa_energy < best_energy:
            # guess = guess - step_size * fprime
            print("lower than before")
            # step_size = step_size / 2
            # continue
        else:
            best_energy = qaoa_energy

        # for i in range(iterations):
        #
        #     guess_mixer_angles = rng.uniform(0, 1, n)
        #     guess_cost_angles = rng.uniform(0, 1, n)
        #


        #
        #     best_guess_mixer_angles = guess_mixer_angles
        #     best_guess_cost_angles = guess_cost_angles
        #     highest_energy = qaoa_energy

    # print("highest energy: ", highest_energy)
    # print("best guess mixer angles: ", best_guess_mixer_angles)
    # print("best guess cost angles: ", best_guess_cost_angles)
    best_guess_mixer_angles = guess[:n]
    best_guess_cost_angles = guess[n:]
    # best_guess_mixer_angles = result.x[:n]
    # best_guess_cost_angles = result.x[n:]
    return best_guess_mixer_angles, best_guess_cost_angles


def qaoa_calculate(
        backend: Backend,
        compiler_pass: Callable[[Circuit], bool],
        shots: int = 5000,
        iterations: int = 100,
        seed: int = 12345,
) -> float:
    # find the parameters for the highest energy
    best_mixer, best_cost = qaoa_optimise_energy(
        compiler_pass, backend, iterations, 3, shots=shots, seed=seed
    )

    # get the circuit with the final parameters of the optimisation:
    my_qaoa_circuit = qaoa_max_cut_circuit(
        max_cut_graph_edges, n_nodes, best_mixer, best_cost
    )

    my_qaoa_circuit.measure_all()

    compiler_pass(my_qaoa_circuit)
    handle = backend.process_circuit(my_qaoa_circuit, shots, seed=seed)

    result = backend.get_result(handle)

    return result


from pytket.extensions.qiskit import AerBackend

backend = AerBackend()
comp = backend.get_compiled_circuit

res = qaoa_calculate(
    backend,
    backend.default_compilation_pass(2).apply,
    shots=5000,
    iterations=100,
    seed=12345,
)

from maxcut_plotting import plot_maxcut_results

plot_maxcut_results(res, 6)
