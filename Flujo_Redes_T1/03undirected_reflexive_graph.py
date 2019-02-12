import networkx as nx
import matplotlib.pyplot as plt

H=nx.Graph()

H.add_nodes_from([0,1,2,3,4],)

H.add_edges_from([(0,1),(0,2),(1,2),(0,3),(0,4),(3,3)])

nx.draw(H,with_labels=True)
plt.savefig("Graph03.eps", format="EPS")
plt.show()