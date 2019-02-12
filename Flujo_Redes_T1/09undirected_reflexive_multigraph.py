import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiGraph()
M.add_nodes_from(["A","B","C","D","E"])

M.add_edges_from([("A","A"),("A","B"),("A","B"),("A","C"),("A","C"),("B","C"),("B","D"),("C","E"),("D","E")])

nx.draw(M,with_labels=True)
plt.savefig("Graph09.eps", format="EPS")
plt.show()