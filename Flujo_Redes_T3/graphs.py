import networkx as nx
import matplotlib.pyplot as plt
import time
import numpy as np
from scipy import stats

replicas_number=19000

######################################### all_shortest_paths  ########################################################

P=nx.Graph()

P.add_nodes_from(['x1','x2','x3','x4','x5'])

P.add_edge('x1','x5',weight=1)
P.add_edge('x1','x4',weight=2)
P.add_edge('x4','x2',weight=2)
P.add_edge('x5','x2',weight=1)
P.add_edge('x2','x3',weight=8)
P.add_edge('x1','x2',weight=8)

pos=nx.kamada_kawai_layout(P)

replicas_asp=[]
for j in range(30):
    start=time.time()
    for i in range (replicas_number):
        nx.all_shortest_paths(P,source='x1',target='x3',weight='weight')
    end=time.time()
    execution_time=end-start
    replicas_asp.append(execution_time)

normality_test=stats.shapiro(replicas_asp)
print(normality_test)
print(replicas_asp)

hist, bin_edges=np.histogram(replicas_asp,density=True)
first_edge, last_edge = np.min(replicas_asp),np.max(replicas_asp)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(asp,bins=bin_edges,rwidth=0.75)
plt.xlabel('Computation time')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig("Histogram_asp.eps", format="EPS")
plt.show(1)

#nx.draw(P,pos=pos,with_labels=True)
#plt.savefig("Graph10.eps", format="EPS")
#plt.show(1)

############################################ Betweenness Centrality ###################################################

B = nx.DiGraph()
B.add_node('DEPOT')
B.add_nodes_from(['Job1','Job2','Job3','Job6'])
B.add_nodes_from(['Job4','Job5','Job7'])
B.add_nodes_from(['Job8','Job9'])

B.add_path(['DEPOT','Job1','Job2','Job3','Job6','DEPOT'])  #Construct a path from the nodes in that order
B.add_path(['DEPOT','Job4','Job5','Job7','DEPOT'])
B.add_path(['DEPOT','Job8','Job9','DEPOT'])

replicas_bc=[]
for j in range(30):
    start=time.time()
    for i in range (replicas_number):
        bw_centrality = nx.betweenness_centrality(B, normalized=False)
    end=time.time()
    execution_time=end-start
    replicas_bc.append(execution_time)

normality_test=stats.shapiro(replicas_bc)
print(normality_test)
print(replicas_bc)

hist, bin_edges=np.histogram(replicas_bc,density=True)
first_edge, last_edge = np.min(replicas_bc),np.max(replicas_bc)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_bc,bins=bin_edges,rwidth=0.75)
plt.xlabel('Computation time')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show(2)

#pos=nx.shell_layout(Be)
#nx.draw(Be,pos=pos,with_labels=True)
#plt.savefig("Graph05.eps", format="EPS")
#plt.show(8)

################################################## dfs_tree #########################################################

D = nx.Graph()

D.add_node('Libro')
D.add_nodes_from(['C1','C2','C3'])
D.add_nodes_from(['s1.1','s1.2','s2.1','s2.2','s2.3'])
D.add_nodes_from(['s2.1.1','s2.1.2'])

D.add_edges_from([('Libro','C1',),('Libro','C2',),('Libro','C3')])
D.add_edges_from([('C1','s1.1',),('C1','s1.2',)])
D.add_edges_from([('C2','s2.1',),('C2','s2.2',),('C2','s2.3')])
D.add_edges_from([('s2.1','s2.1.1'),('s2.1','s2.1.2')])

replicas_dfs=[]
for j in range(30):
    start=time.time()
    for i in range (replicas_number):
        dfs = nx.dfs_tree(D)
    end=time.time()
    execution_time=end-start
    replicas_dfs.append(execution_time)

normality_test=stats.shapiro(replicas_dfs)
print(normality_test)
print(replicas_dfs)

hist, bin_edges=np.histogram(replicas_dfs,density=True)
first_edge, last_edge = np.min(replicas_dfs),np.max(replicas_dfs)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_dfs,bins=bin_edges,rwidth=0.75)
plt.xlabel('Computation time')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show(3)

#nx.draw(D,with_labels=True)
#plt.savefig("Graph01.eps", format="EPS")
#plt.show(3)

#####################################strongly_connected_components ###################################################

S=nx.DiGraph()
S.add_nodes_from(['A','B','C','D','E'])

S.add_edges_from([('A','B'),('A','C'),('B','C'),('A','D'),('A','E'),('D','D')])

color_map = []
for node in S:
    if (node == 'D'):
        color_map.append('blue')
    else:
        color_map.append('red')

pos = nx.kamada_kawai_layout(S)

replicas_scc=[]
for j in range(30):
    start=time.time()
    for i in range (replicas_number):
        sccs = list(nx.strongly_connected_components(S))
    end=time.time()
    execution_time=end-start
    replicas_scc.append(execution_time)

normality_test=stats.shapiro(replicas_scc)
print(normality_test)
print(replicas_scc)

hist, bin_edges=np.histogram(replicas_scc,density=True)
first_edge, last_edge = np.min(replicas_scc),np.max(replicas_scc)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_scc,bins=bin_edges,rwidth=0.75)
plt.xlabel('Computation time')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show(4)

#nx.draw(S,pos=pos,node_color=color_map,with_labels=True)
#plt.savefig("Graph03.eps", format="EPS")
#plt.show(4)

################################################ topological_sort #####################################################

T = nx.DiGraph()

T.add_nodes_from(['r','t','u','v','w','x','y','z'])

T.add_edges_from([('x','y'),('r','t'),('t','v'),('t','u'),('u','w'),('x','z'),('y','z'),('y','v'),('v','w'),
                  ('v','x'),('x','z'),('z','v'),('z','w')],color='black',weight=1)

edges = T.edges()

colors = []
weight = []

for (u,v,attrib_dict) in list(T.edges.data()):
    colors.append(attrib_dict['color'])
    weight.append(attrib_dict['weight'])

pos = nx.shell_layout(T)

replicas_ts=[]
for j in range(30):
    start=time.time()
    for i in range (replicas_number):
        ts = nx.topological_sort(T)
    end=time.time()
    execution_time=end-start
    replicas_ts.append(execution_time)

normality_test=stats.shapiro(replicas_ts)
print(normality_test)
print(replicas_ts)

hist, bin_edges=np.histogram(replicas_ts,density=True)
first_edge, last_edge = np.min(replicas_ts),np.max(replicas_ts)

n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(replicas_ts,bins=bin_edges,rwidth=0.75)
plt.xlabel('Computation time')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show(5)

#nx.draw(T,pos=pos,edges=edges,edge_color=colors,width=weight,with_labels=True)
#plt.savefig("Graph07.eps", format="EPS")
#plt.show(5)

################################################################################################################

fig = plt.subplots(nrows=1, ncols=1, sharey=False)

algorithm_dataset=[replicas_asp,replicas_bc,replicas_dfs,replicas_scc,replicas_ts]

labels = ['all_shortest_paths', 'betweenness_centrality', 'dfs_tree',
          'strongly_connected_components', 'topological_sort']

parts = plt.violinplot(algorithm_dataset, positions=[1,2,3,4,5],
                       showmeans=True, showmedians=True, showextrema=True)

plt.show(6)
