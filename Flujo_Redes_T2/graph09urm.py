import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiGraph()
M.add_nodes_from(["A","B","C","D","E"])

M.add_edges_from([("A","B"),("A","C")],color='blue', weight=8)
M.add_edges_from([("A","A"),("A","B"),("A","C"),("B","C"),("B","D"),("C","E"),("D","E")], color='black', weight=2)

edges = M.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(M.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

g=nx.shell_layout(M)
nx.draw(M,edges=edges,pos=g,edge_color=colors,width=weight,with_labels=True)
#plt.savefig("Graph09.eps", format="EPS")
plt.show()