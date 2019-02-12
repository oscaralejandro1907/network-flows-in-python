import networkx as nx
import matplotlib.pyplot as plt

M = nx.MultiGraph()                                 #Create an empty Multigraph

M.add_nodes_from(['X','Y','Z','V','W'])
M.add_edges_from([('X','Y'),('X','Y'),('Y','Z'),('Z','V'),('V','W')])

nx.draw(M,with_labels=True)
plt.savefig("Graph07.eps", format="EPS")
plt.show()

