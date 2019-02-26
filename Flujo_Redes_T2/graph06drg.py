import networkx as nx
import matplotlib.pyplot as plt

R=nx.DiGraph()
R.add_nodes_from(["D","1","2","3","4"])

R.add_edges_from([("D","1"),("1","2"),("2","D")])
R.add_edges_from([("D","3"),("3","4"),("4","D"),("D","D")])

color_map = []
for node in R:
    if (node == "D"):
        color_map.append('blue')
    else:
        color_map.append('red')

nx.draw(R,node_color=color_map,pos=nx.random_layout(R),with_labels=True)
plt.savefig("Graph06.eps", format="EPS")
plt.show()