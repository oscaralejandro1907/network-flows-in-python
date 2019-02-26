import networkx as nx
import matplotlib.pyplot as plt

G=nx.DiGraph()                                  #Create an empty directed graph
G.add_node("X")
G.add_nodes_from(["R1","R2","R3","R4"])

G.add_edges_from([("X","R1"),("X","R2"),("X","R3"),("X","R4")])

pos=nx.fruchterman_reingold_layout(G,k=0.2,iterations=30)

nx.draw(G,pos=pos,node_color='skyblue',with_labels=True)
plt.savefig("Graph04.eps", format="EPS")
plt.show()