import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiDiGraph()

M.add_nodes_from(["Depot","Warehouse1","Warehouse2","Warehouse3","Warehouse4"])

M.add_edges_from([("Depot","Warehouse1"),("Depot","Warehouse1"),("Depot","Warehouse2"),("Depot","Warehouse3"),("Depot","Warehouse4"),("Depot","Depot")])

nx.draw(M,with_labels=True)
plt.savefig("Graph12.eps", format="EPS")
plt.show()