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

import pickle


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
    # load subgraphs from file
    found = True

    try:
        x = pickle.load(open("subgraphs3.pkl", "rb"))
    except:
        found = False
    if found:
        found = input(
            "Input y to use existing subgraphs, else will generate new ones: ")
    if found:
        return x
    else:
        res = x  # Continue from savepoint

        for j in range(100):
            for t in range(20, 40, 2):
                G = nx.random_regular_graph(3, t)
                for edge in G.edges():
                    subgraph = subgraphInduce(G, edge, 2)
                    seen = False
                    for j in range(len(res)):
                        if nx.is_isomorphic(subgraph, res[j][0]):
                            seen = True
                            res[j][1] += 1
                            break
                    if not seen:
                        # print(len(res))
                        res.append([subgraph, 1])
                        # res.append(subgraph)
                res = sorted(res, key=lambda x: x[1])

            print("Generated Subgraphs len = ", len(res), "Sorted by size = ", " ".join(
                map(str, sorted([(i[1], len(i[0].edges)) for i in res])[:-100:-1])))
        for j in range(1000):
            for t in range(20, 100, 2):
                G = nx.random_regular_graph(3, t)
                for edge in G.edges():
                    subgraph = subgraphInduce(G, edge, 2)
                    seen = False
                    for j in range(len(res)):
                        if nx.is_isomorphic(subgraph, res[j][0]):
                            seen = True
                            res[j][1] += 1
                            break
                    if not seen:
                        # print(len(res))
                        res.append([subgraph, 1])
                        # res.append(subgraph)
                # sort by size
                res = sorted(res, key=lambda x: x[1])
            print("Generated Subgraphs len = ", len(res), "Sorted by size = ", " ".join(
                map(str, sorted([(i[1], len(i[0].edges)) for i in res])[:-100:-1])))

            pickle.dump(res, open("subgraphs3.pkl", "wb"))


gimme_subgraphs()
