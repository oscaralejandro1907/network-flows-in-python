import networkx as nx
import matplotlib.pyplot as plt

R=nx.DiGraph()
R.add_nodes_from(["DEPOT","1","2","3","4"])

R.add_edges_from([("DEPOT","1"),("1","2"),("2","DEPOT")])
R.add_edges_from([("DEPOT","3"),("3","4"),("4","DEPOT"),("DEPOT","DEPOT")])

nx.draw(R,with_labels=True)
plt.savefig("Graph06.eps", format="EPS")
plt.show()