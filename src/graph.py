import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


def drawGraph(relationArray):
    G = nx.DiGraph()
    G.add_edges_from(relationArray)
    # for x in relationArray:
    #     G.add_edge(x[0],x[1],len=20)
    pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", args="", root="StartPoint")
    options = {"with_labels": True, "alpha": 1, "node_size": 100, "font_size": 10}
    plt.figure(figsize=(100, 100))
    nx.draw(G, pos, node_color="r", **options)

    plt.axis("equal")
    plt.savefig("path.png")
