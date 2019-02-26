import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiDiGraph()

M.add_nodes_from(["Depot","Warehouse1","Warehouse2","Warehouse3","Warehouse4"])

M.add_edges_from([("Depot","Warehouse1"),("Depot","Warehouse1"),("Depot","Warehouse2"),("Depot","Warehouse3"),("Depot","Warehouse4"),("Depot","Depot")])

color_map = []
for node in M:
    if (node == 3):
        color_map.append('blue')
    else:
        color_map.append('red')

pos=nx.shell_layout(M)

nx.draw(M,pos=pos,node_color=color_map,with_labels=True)
plt.savefig("Graph12.eps", format="EPS")
plt.show()