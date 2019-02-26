import networkx as nx
import matplotlib.pyplot as plt

M = nx.MultiGraph()                                 #Create an empty Multigraph

M.add_nodes_from(['x','y','z','v','w'])

M.add_edge('x','y',color='blue',weight=6)
M.add_edges_from([('x','y'),('x','y'),('y','z'),('z','v'),('v','w')],color='black',weight=1)

edges = M.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(M.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

pos = nx.fruchterman_reingold_layout(M,k=0.15,iterations=20)

nx.draw(M,pos=pos,edges=edges,edge_color=colors,width=weight,with_labels=True)
plt.savefig("Graph07.eps", format="EPS")
plt.show()

