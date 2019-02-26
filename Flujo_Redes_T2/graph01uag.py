import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

G = nx.Graph()                                          #Create an empty graph

G.add_node('Libro')                                     #Add a simple node
G.add_nodes_from(['C1','C2','C3'])                      #Add a list of nodes
G.add_nodes_from(['s1.1','s1.2','s2.1','s2.2','s2.3'])
G.add_nodes_from(['s2.1.1','s2.1.2'])

G.add_edges_from([('Libro','C1',),('Libro','C2',),('Libro','C3')])
G.add_edges_from([('C1','s1.1',),('C1','s1.2',)])
G.add_edges_from([('C2','s2.1',),('C2','s2.2',),('C2','s2.3')])
G.add_edges_from([('s2.1','s2.1.1'),('s2.1','s2.1.2')])

#Consulted at: |https://github.com/bhargavchippada/forceatlas2
forceatlas2 = ForceAtlas2(
                        # Behavior alternatives
                        outboundAttractionDistribution=True,  # Dissuade hubs
                        linLogMode=False,
                        adjustSizes=False,
                        edgeWeightInfluence=1.0,

                        # Performance
                        jitterTolerance=1.0,
                        barnesHutOptimize=True,
                        barnesHutTheta=1.2,
                        multiThreaded=False,

                        # Tuning
                        scalingRatio=2.0,
                        strongGravityMode=False,
                        gravity=1.0,

                        # Log
                        verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=2000)

nx.draw_networkx_nodes(G, positions, node_size=100, with_labels=True, node_color="red", alpha=0.4)
nx.draw_networkx_edges(G, positions, edge_color="black", alpha=0.05)
plt.axis('off')
plt.savefig("Graph01.eps", format="EPS")
plt.show()