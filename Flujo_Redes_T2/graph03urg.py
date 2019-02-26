import networkx as nx
import matplotlib.pyplot as plt

H=nx.Graph()
H.add_nodes_from([0,1,2])
H.add_nodes_from([3,4])

H.add_edges_from([(0,1),(0,2),(1,2),(0,3),(0,4),(3,3)])

color_map = []
for node in H:
    if (node == 3):
        color_map.append('blue')
    else:
        color_map.append('red')

pos = nx.kamada_kawai_layout(H)

nx.draw(H,pos=pos,node_color=color_map,with_labels=True)
plt.savefig("Graph03.eps", format="EPS")
plt.show()