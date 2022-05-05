import networkx as nx
import matplotlib.pyplot as plt


def drawGraph(relationArray):
    G = nx.DiGraph()
    G.add_edges_from(relationArray)

    nx.draw(G, with_labels=True)

    plt.show()
