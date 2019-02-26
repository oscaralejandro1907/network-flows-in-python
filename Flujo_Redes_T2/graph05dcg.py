import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_node('DEPOT')
G.add_nodes_from(['Job1','Job2','Job3','Job6'])
G.add_nodes_from(['Job4','Job5','Job7'])
G.add_nodes_from(['Job8','Job9'])

G.add_path(['DEPOT','Job1','Job2','Job3','Job6','DEPOT'])  #Construct a path from the nodes in that order
G.add_path(['DEPOT','Job4','Job5','Job7','DEPOT'])
G.add_path(['DEPOT','Job8','Job9','DEPOT'])

pos=nx.shell_layout(G)
nx.draw(G,pos=pos,with_labels=True)
plt.savefig("Graph05.eps", format="EPS")
plt.show()