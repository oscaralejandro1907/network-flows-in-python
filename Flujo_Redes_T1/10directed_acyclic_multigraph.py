import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiDiGraph()                       #Create an empty directed multigraph

M.add_nodes_from(["x1","x2","x3","x4","x5"])

M.add_edges_from([("x1","x2"),("x1","x2"),("x3","x2"),("x4","x3"),("x4","x2"),("x5","x2")])

nx.draw(M,with_labels=True)
plt.savefig("Graph10.eps", format="EPS")
plt.show()