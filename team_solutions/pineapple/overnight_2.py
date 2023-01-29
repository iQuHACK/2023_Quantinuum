import os
from matplotlib import pyplot as plt
from pytket.extensions.qiskit import AerBackend
from pytket.backends.backend import Backend
from pytket.backends.backendresult import BackendResult
from pytket.passes import DecomposeBoxes
from pytket.utils import gen_term_sequence_circuit
import numpy as np
from pytket import Qubit, Circuit
from pytket.pauli import QubitPauliString, Pauli
from pytket.utils import QubitPauliOperator
from typing import List, Tuple, Callable
import networkx as nx
import networkx.algorithms.isomorphism.vf2userfunc as vf2
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import networkx.algorithms.isomorphism.vf2userfunc as vf2

import time

import pickle


def single_edge_energy(results: BackendResult) -> float:
    """
    Return the expected enery of a edge 0-1.
    """
    dist = results.get_distribution()
    return sum((meas[0] ^ meas[1]) * prob for meas, prob in dist.items())


def subgraphInduce(G, edge, depth, rename=True):
    # return: subgraph induced by edge
    current = set(edge)
    edges = set([edge])
    for i in range(depth):
        next = set()
        for node in current:
            next.update(G.neighbors(node))
            edges.update(G.edges(node))
        current.update(next)
    if rename:
        # Rename nodes to 0, 1, 2, ... such that 0 and 1 are the central edge.
        current.remove(edge[0])
        current.remove(edge[1])
        current = [edge[0], edge[1]] + list(current)

        edges = [(current.index(e[0]), current.index(e[1]))
                 for e in edges]
    return nx.Graph(list(edges))


SUBGRAPHS = pickle.load(open("subgraphs.pkl", "rb"))
needed = [22, 20, 13]
SUBGRAPHS = [SUBGRAPHS[i] for i in needed]
# print(len(SUBGRAPHS))
# for i in SUBGRAPHS:
#     print(i)


def qaoa_initial_circuit(n_qubits: int) -> Circuit:
    c = Circuit(n_qubits)
    for i in range(n_qubits):
        c.H(i)
    return c


def qaoa_graph_to_cost_hamiltonian(
    edges: List[Tuple[int, int]], cost_angle: float
) -> QubitPauliOperator:
    """
    This function takes a list of edges and a cost angle and returns a QubitPauliOperator
    representing the cost Hamiltonian for the QAOA algorithm.

    """
    qpo_dict = {QubitPauliString(): len(edges) * 0.5 * cost_angle}
    for e in edges:
        term_string = QubitPauliString(
            [Qubit(e[0]), Qubit(e[1])], [Pauli.Z, Pauli.Z])
        qpo_dict[term_string] = -0.5 * cost_angle
    return QubitPauliOperator(qpo_dict)


def qaoa_max_cut_circuit(
    edges: List[Tuple[int, int]],
    mixer_angles: List[float],
    cost_angles: List[float],
) -> Circuit:
    """
    Create a QAOA circuit for the MaxCut problem.
    """

    n_nodes: int = len(set().union(*edges))

    # print(len(mixer_angles), len(cost_angles))

    assert len(mixer_angles) == len(cost_angles)

    # initial state
    qaoa_circuit = qaoa_initial_circuit(n_nodes)

    # add cost and mixer terms to state
    for cost, mixer in zip(cost_angles, mixer_angles):
        cost_ham = qaoa_graph_to_cost_hamiltonian(edges, cost)
        mixer_ham = QubitPauliOperator(
            {QubitPauliString([Qubit(i)], [Pauli.X])
                              : mixer for i in range(n_nodes)}
        )
        qaoa_circuit.append(gen_term_sequence_circuit(
            cost_ham, Circuit(n_nodes)))
        qaoa_circuit.append(gen_term_sequence_circuit(
            mixer_ham, Circuit(n_nodes)))

    DecomposeBoxes().apply(qaoa_circuit)
    return qaoa_circuit


def single_precompute(graph, backend, compiler_pass, shots, discretization, seed):
    """
    This function precomputes the results for a small k-regular graphs for many angles.
    For instance, if discretization = (10, 10, 10, 10) [param_num = 4]
    Then we will return results for mixer_angles = (i/10, j/10) and
    cost_angles = (k/10, l/10) for all i, j, k, l in {0, ..., 9}
    These are formatted as [*mixer_angles, *cost_angles]

    """
    # print(discretization)
    results = np.zeros(discretization)
    for index in np.ndindex(*discretization):
        true_index = np.array(index) / discretization  # normalize to [0, 1]
        mixer_angles = true_index[:len(index) // 2]
        cost_angles = true_index[len(index) // 2:]

        # get the circuit with the final parameters of the optimisation:
        circuit = qaoa_max_cut_circuit(
            graph, mixer_angles, cost_angles
        )

        circuit.measure_all()

        compiler_pass(circuit)
        handle = backend.process_circuit(circuit, shots, seed=seed)
        res = single_edge_energy(backend.get_result(handle))
        if (sum(index[1:]) == 0):
            print("Angles", mixer_angles, cost_angles)
            # time.sleep(5)  # cool down.
        # print("Angles", mixer_angles, cost_angles, "Energy:", res)

        results[index] = res
    return results


def filename(graph):
    h = "".join(str(i[0]) + str(i[1]) for i in graph)
    return h


def precompute(backend, compiler_pass, shots, discretization, seed):
    # precompute the results for all graphs
    """
    This function precomputes the results for a small k-regular graphs for many angles.
    For now we only precompute for a hardcoded list of k = 3, p = 1.
    Node 0 = j, Node 1 = k.
    """
    # TODO: don't cheat.

    for graph in SUBGRAPHS:
        # Check if we have already computed this graph
        if os.path.exists(filename(graph) + ".pkl"):
            print("Skipping", graph)
            continue

        now = time.time()
        print(now)
        print("subgraph: ", graph)
        x = single_precompute(
            graph, backend, compiler_pass, shots, discretization, seed
        )

        what = filename(graph)

        pickle.dump(x, open(str(what) + ".pkl", "wb"))

        print("Maximum Energy: ", np.max(x))
        print(time.time() - now)


# y = pickle.load(open("7073760102818118101112925114.pkl", "rb"))
# print(y.shape)
# print(y)

print(len(SUBGRAPHS))
print(len(set([filename(i) for i in SUBGRAPHS])))
backend = AerBackend()
comp = backend.get_compiled_circuit


DISCRETIZATION = (10, 10, 10, 10)

PRECOMPUTE = precompute(backend,
                        backend.default_compilation_pass(0).apply,
                        5000, DISCRETIZATION, 12345)
