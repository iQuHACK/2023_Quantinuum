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

import pickle


SUBGRAPHS = pickle.load(open("subgraphs.pkl", "rb"))

print(len(SUBGRAPHS))
for i in SUBGRAPHS:
    print(i)


def filename(graph):
    h = "".join(str(i[0]) + str(i[1]) for i in graph)
    return h

# Collect all subgraphs into one file


results = []

for i, graph in enumerate(SUBGRAPHS):
    # Check if we have already computed this graph
    if os.path.exists(str(filename(graph)) + ".pkl"):
        results.append(pickle.load(open(str(filename(graph)) + ".pkl", "rb")))
        print(i, "#", len(results))
        x = results[-1]
        # print(x.shape)
        # rft = np.fft.rfftn(x)
        # rft[4:, :, :, :] = 0
        # rft[:, 4:, :, :] = 0
        # rft[:, :, 4:, :] = 0
        # rft[:, :, :, 4:] = 0

        # x_smooth = np.fft.irfftn(rft)
        # # Sum along last two axes ( we are left with mixer )
        # visualize_x = np.sum(x, axis=(2, 3))
        # visualize_x_smooth = np.sum(x_smooth, axis=(2, 3))

        # # Sum along the first two axes ( we are left with cost )
        # visualize_y = np.sum(x, axis=(0, 1))
        # visualize_y_smooth = np.sum(x_smooth, axis=(0, 1))

        # f, axarr = plt.subplots(2, 2)
        # axarr[0][0].imshow(visualize_x, cmap="hot", interpolation="nearest")
        # axarr[0][1].imshow(visualize_x_smooth, cmap="hot",
        #                    interpolation="nearest")
        # axarr[1][0].imshow(visualize_y, cmap="hot", interpolation="nearest")
        # axarr[1][1].imshow(visualize_y_smooth, cmap="hot",
        #                    interpolation="nearest")

        # plt.show()
    else:
        results.append(None)
        print(i, "X")

pickle.dump(results, open("p2data.pkl", "wb"))
