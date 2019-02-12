import networkx as nx
import matplotlib.pyplot as plt

M=nx.MultiDiGraph()
M.add_nodes_from(["Coahuila","Sonora","Guanajuato","Veracruz","Quintana_Roo",])

M.add_edges_from([("Coahuila","Sonora"),("Sonora","Coahuila"),("Coahuila","Guanajuato"),("Guanajuato","Veracruz"),("Veracruz","Quintana_Roo"),("Quintana_Roo","Coahuila")])

nx.draw(M,with_labels=True)
plt.savefig("Graph11.eps", format="EPS")
plt.show()

