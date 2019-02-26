import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiDiGraph()
M.add_nodes_from(["Coahuila","Veracruz"], bipartite=0)
M.add_nodes_from(["Sonora","Guanajuato","Quintana_Roo"], bipartite=1)

M.add_edge("Sonora","Coahuila", color='blue', weight=1)
M.add_edges_from([("Coahuila","Sonora"),("Coahuila","Guanajuato"),("Guanajuato","Veracruz"),("Veracruz","Quintana_Roo"),("Quintana_Roo","Coahuila")],color='black', weight=1)

edges = M.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(M.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

nx.draw(M,pos=nx.bipartite_layout(M,["Coahuila","Veracruz"]),edges=edges,edge_color=colors,width=weight,with_labels=True)
plt.savefig("Graph11.eps", format="EPS")
plt.show()

