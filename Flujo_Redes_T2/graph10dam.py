import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiDiGraph()                       #Create an empty directed multigraph

M.add_nodes_from(["x1","x2","x3","x4","x5"])

M.add_edge("x1","x2",color='green',weight=6)
M.add_edges_from([("x1","x2"),("x3","x2"),("x4","x3"),("x4","x2"),("x5","x2")],color='black',weight=1)

edges = M.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(M.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

pos=nx.kamada_kawai_layout(M)

nx.draw(M,pos=pos,edges=edges,edge_color=colors,width=weight,with_labels=True)
plt.savefig("Graph10.eps", format="EPS")
plt.show()