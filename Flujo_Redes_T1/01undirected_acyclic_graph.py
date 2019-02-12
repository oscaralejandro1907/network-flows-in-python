import networkx as nx                                   #Library to create graphs
import matplotlib.pyplot as plt                         #Library to show graphs

G = nx.Graph()                                          #Create an empty graph

G.add_node('Libro')                                     #Add a simple node
G.add_nodes_from(['C1','C2','C3'])                      #Add a list of nodes
G.add_nodes_from(['s1.1','s1.2','s2.1','s2.2','s2.3'])
G.add_nodes_from(['s2.1.1','s2.1.2'])

G.add_edges_from([('Libro','C1',),('Libro','C2',),('Libro','C3')])   #Add a list of edges
G.add_edges_from([('C1','s1.1',),('C1','s1.2',)])
G.add_edges_from([('C2','s2.1',),('C2','s2.2',),('C2','s2.3')])
G.add_edges_from([('s2.1','s2.1.1'),('s2.1','s2.1.2')])

nx.draw(G,with_labels=True)                            #Draw the Graph named G
plt.savefig("Graph01.eps", format="EPS")               #Save figure in eps format
plt.show()                                             #Show (Print) Graph