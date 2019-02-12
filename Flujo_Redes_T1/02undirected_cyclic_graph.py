import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_nodes_from(['A','B','C','D','E'])

G.add_edges_from([('A','B'),('B','C'),('C','D'),('D','E'),('E','A')])

nx.draw(G,with_labels=True)
plt.savefig("Graph02.eps", format="EPS")
plt.show()