import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiGraph()

M.add_nodes_from([1,2,3,4,5])

M.add_edge(2,1, color='blue',weight=6)
M.add_edges_from([(1,2),(1,3),(3,4),(4,5),(5,1)],color='black', weight=1)

edges = M.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(M.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

pos = nx.spring_layout(M, scale=3)

nx.draw(M,pos,edges=edges,edge_color=colors,width=weight,with_labels=True, font_size=8, font_family='sans-serif')
plt.savefig("Graph08.eps", format="EPS")
plt.show()