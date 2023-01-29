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
import os
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


x = pickle.load(open("subgraphs3.pkl", "rb"))  # Subgraphs with frequency

our_subgraphs = pickle.load(open("subgraphs.pkl", "rb"))  # Subgraphs

print(len(our_subgraphs))
freq = []
for idx, subgraph in enumerate(our_subgraphs):
    found = False
    for i in x:
        if nx.is_isomorphic(i[0], nx.Graph(subgraph)):
            found = True
            freq.append([idx, i[1]])
            break
    if not found:
        freq.append([idx, 0])


def filename(graph):
    h = "".join(str(i[0]) + str(i[1]) for i in graph)
    return h


print(len(freq))
freq = sorted(freq, key=lambda x: x[1], reverse=True)
print("\n".join([str(i) for i in freq]))

# Figure out which ones we urgently need to find
for i, f in freq:
    if not os.path.exists(str(filename(our_subgraphs[i])) + ".pkl"):
        print("FUCK", i, f)
