import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiGraph()

M.add_nodes_from([1,2,3,4,5])

M.add_edges_from([(1,2),(2,1),(1,3),(3,4),(4,5),(5,1)])

nx.draw(M,with_labels=True)
plt.savefig("Graph08.eps", format="EPS")
plt.show()