import pennylane as qml
from pennylane import numpy as np
import networkx as nx
from networkx.generators import gnp_random_graph
from networkx.drawing import draw

from matplotlib import use as mpl_use

mpl_use("module://matplotlib-backend-sixel")

import matplotlib.pyplot as plt

seed = 0
n = 6
k = 4 # colors

qdevice: qml.QubitDevice = qml.device('default.qubit')  # type: ignore

graph: nx.Graph = gnp_random_graph(n=n, p=0.5, seed=seed)

draw(graph)
plt.show()
print()

edges = []
for n1, neighbors in graph.adjacency():
    for n2 in neighbors:
        edge = sorted([n1, n2])
        if edge not in edges:
            edges.append(edge)


