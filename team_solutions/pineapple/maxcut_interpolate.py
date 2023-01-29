from matplotlib import pyplot as plt
from maxcut_plotting import plot_maxcut_results
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


def gimme_subgraphs():
    res = []

    for t in range(20, 100, 2):
        G = nx.random_regular_graph(3, t)
        for edge in G.edges():
            subgraph = subgraphInduce(G, edge, 2)
            seen = False
            for i in res:
                if nx.is_isomorphic(subgraph, i):
                    seen = True
                    # res[i][1] += 1
                    break
            if not seen:
                # print(len(res))
                # res.append([subgraph, 1])
                res.append(subgraph)
    print("Generated Subgraphs len = ", len(res))
    return [list(i.edges) for i in res]


# res = sorted(res, key=lambda x: x[1], reverse=True)
# for i in range(100):
#    print(res[i][1])
# nx.draw(G)
# plt.show()


# Define graph.
# TOOD: Hardcoded for now, but should be able to take any p, k
# SUBGRAPHS = [
#     [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)],
#     [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4)],
#     [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5)],
# ]


SUBGRAPHS = gimme_subgraphs()
print(SUBGRAPHS[0])
print(len(SUBGRAPHS))


NX_SUBGRAPHS = [nx.Graph(e) for e in SUBGRAPHS]

P_DISTANCE = 2  # TODO: Hardcoded for now, but should be able to take any p, k
K_BRANCHING = 3  # TODO: Hardcoded for now, but should be able to take any p, k

DISCRETIZATION = (4, 4, 4, 4)

n_nodes = 24


max_cut_graph = nx.random_regular_graph(K_BRANCHING, n_nodes)


# nx.draw(max_cut_graph, labels={node: node for node in max_cut_graph.nodes()})
# plt.show()

max_cut_graph_edges = max_cut_graph.edges()


# max_cut_graph = nx.Graph()
# max_cut_graph.add_edges_from(max_cut_graph_edges)
# nx.draw(max_cut_graph, labels={node: node for node in max_cut_graph.nodes()})

# expected_results = [(0, 1, 0, 0, 1, 0, 0), (1, 0, 1, 1, 0, 1, 1)]


def get_subgraph_frequency(nx_graph):
    """
    Find the frequency of each subgraph in the graph.
    """
    subgraph_freq = np.zeros((len(NX_SUBGRAPHS),))
    for central_edge in nx_graph.edges:
        neighborhood = subgraphInduce(
            nx_graph, central_edge, P_DISTANCE)
        for i, subgraph in enumerate(NX_SUBGRAPHS):
            if nx.is_isomorphic(neighborhood, subgraph):
                subgraph_freq[i] += 1
    print(subgraph_freq)
    return subgraph_freq


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


cost_angle = 1.0
cost_ham_qpo = qaoa_graph_to_cost_hamiltonian(max_cut_graph_edges, cost_angle)
print(cost_ham_qpo)


def qaoa_initial_circuit(n_qubits: int) -> Circuit:
    c = Circuit(n_qubits)
    for i in range(n_qubits):
        c.H(i)
    return c


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
            {QubitPauliString([Qubit(i)], [Pauli.X])             : mixer for i in range(n_nodes)}
        )
        qaoa_circuit.append(gen_term_sequence_circuit(
            cost_ham, Circuit(n_nodes)))
        qaoa_circuit.append(gen_term_sequence_circuit(
            mixer_ham, Circuit(n_nodes)))

    DecomposeBoxes().apply(qaoa_circuit)
    return qaoa_circuit


def max_cut_energy(edges: List[Tuple[int, int]], results: BackendResult, maximize=False) -> float:
    """
    Given the results of all shots:
    - if maximize is False, return the average energy of the distribution (used for training)
    - if maximize is True, return the maximum energy of the distribution (used for testing)
    """
    energy = 0.0
    dist = results.get_distribution()
    if maximize:
        for meas in dist.keys():
            energy = max(energy, sum((meas[i] ^ meas[j]) for i, j in edges))
    else:
        for i, j in edges:
            energy += sum((meas[i] ^ meas[j]) *
                          prob for meas, prob in dist.items())

    return energy


def single_edge_energy(results: BackendResult) -> float:
    """
    Return the expected enery of a edge 0-1.
    """
    dist = results.get_distribution()
    return sum((meas[0] ^ meas[1]) * prob for meas, prob in dist.items())


def qaoa_instance_simple(
    graph_edges: List[Tuple[int, int]],
    backend: Backend,
    compiler_pass: Callable[[Circuit], bool],
    guess_mixer_angles: np.array,
    guess_cost_angles: np.array,
    seed: int,
    shots: int = 5000,
) -> float:
    # step 1: get state guess
    my_prep_circuit = qaoa_max_cut_circuit(
        graph_edges, guess_mixer_angles, guess_cost_angles
    )

    measured_circ = my_prep_circuit.copy().measure_all()
    compiler_pass(measured_circ)
    res = backend.run_circuit(measured_circ, shots, seed=seed)

    return max_cut_graph_edges, res


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
        # print("Angles", mixer_angles, cost_angles, "Energy:", res)

        results[index] = res
    return results


def precompute(backend, compiler_pass, shots, discretization, seed):
    # precompute the results for all graphs
    """
    This function precomputes the results for a small k-regular graphs for many angles.
    For now we only precompute for a hardcoded list of k = 3, p = 1.
    Node 0 = j, Node 1 = k.
    """
    # TODO: don't cheat.
    x = get_subgraph_frequency(max_cut_graph)

    filter = [i != 0 for i in x]
    print(sum(filter), " out of ", len(filter), " graphs are non-zero.")

    results = []

    for graph, f in zip(SUBGRAPHS, filter):
        if not f:
            results.append(None)
            continue
        print("subgraph: ", graph)
        x = single_precompute(
            graph, backend, compiler_pass, shots, discretization, seed
        )
        results.append(x)
        print("Maximum Energy: ", np.max(x))

        rft = np.fft.rfftn(x)
        rft[4:, :, :, :] = 0
        rft[:, 4:, :, :] = 0
        rft[:, :, 4:, :] = 0
        rft[:, :, :, 4:] = 0

        x_smooth = np.fft.irfftn(rft)
        # Sum along last two axes ( we are left with mixer )
        visualize_x = np.sum(x, axis=(2, 3))
        visualize_x_smooth = np.sum(x_smooth, axis=(2, 3))

        # Sum along the first two axes ( we are left with cost )
        visualize_y = np.sum(x, axis=(0, 1))
        visualize_y_smooth = np.sum(x_smooth, axis=(0, 1))

        f, axarr = plt.subplots(2, 2)
        axarr[0][0].imshow(visualize_x, cmap="hot", interpolation="nearest")
        axarr[0][1].imshow(visualize_x_smooth, cmap="hot",
                           interpolation="nearest")
        axarr[1][0].imshow(visualize_y, cmap="hot", interpolation="nearest")
        axarr[1][1].imshow(visualize_y_smooth, cmap="hot",
                           interpolation="nearest")

        plt.show()

    return results


backend = AerBackend()
comp = backend.get_compiled_circuit


PRECOMPUTE = precompute(backend,
                        backend.default_compilation_pass(0).apply,
                        5000, DISCRETIZATION, 12345)


input()


def optimize_params(nx_graph, discretization):
    """
    This function optimizes the parameters for a given graph.
    """
    best = -np.inf
    best_mixer_angles = None
    best_cost_angles = None

    freq = get_subgraph_frequency(nx_graph)
    print(freq)
    for index in np.ndindex(*discretization):
        score = sum(PRECOMPUTE[sub][index] * freq[sub]
                    for sub in range(len(SUBGRAPHS)) if freq[sub] != 0)
        # print(score)
        # print(best)
        if (score > best):
            best = score

            # normalize to [0, 1]
            true_index = np.array(index) / discretization
            best_mixer_angles = true_index[:len(index) // 2]
            best_cost_angles = true_index[len(index) // 2:]
    return best_mixer_angles, best_cost_angles


def calculateEnergy(
    graph,
    backend: Backend,
    compiler_pass: Callable[[Circuit], bool],
    shots: int = 5000,
    seed: int = 12345,
) -> float:
    """
        Given a graph, first compute the best parameters for the graph.
        Then, run the QAOA circuit with the best parameters.
    """

    # find the parameters for the highest energy
    nx_graph = nx.Graph(graph)
    best_mixer, best_cost = optimize_params(nx_graph, DISCRETIZATION)

    print("Best parameters: ", best_mixer, best_cost)

    # get the circuit with the final parameters of the optimisation:
    circuit = qaoa_max_cut_circuit(
        graph, best_mixer, best_cost
    )

    circuit.measure_all()

    compiler_pass(circuit)
    handle = backend.process_circuit(circuit, shots, seed=seed)

    result = backend.get_result(handle)

    return result


if __name__ == "__main__":
    res = calculateEnergy(
        max_cut_graph_edges,
        backend,
        backend.default_compilation_pass(2).apply,
        shots=100000,
        seed=12345
    )

    dist = res.get_distribution()
    energy_distribution = {}
    energy_colors = {}
    for meas in dist.keys():
        energy = sum((meas[i] ^ meas[j]) for i, j in max_cut_graph_edges)
        if energy not in energy_distribution:
            energy_distribution[energy] = 0
            energy_colors[energy] = []
        energy_distribution[energy] += dist[meas]
        energy_colors[energy].append(meas)

    for i in sorted(energy_distribution.keys()):
        print(i, energy_distribution[i])

    best = max(energy_distribution.keys())
    print("Best energy: ", best)
    coloring = energy_colors[best][0]
    nx.draw(max_cut_graph, labels={node: node for node in max_cut_graph.nodes(
    )}, node_color=["red" if coloring[node] else "blue" for node in max_cut_graph.nodes()])
    plt.show()

    # print(res)

    # plot_maxcut_results(res, 10)
