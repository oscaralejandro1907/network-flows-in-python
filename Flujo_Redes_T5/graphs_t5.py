import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import heapq
import time
import seaborn as sns
import pandas as pd
import collections
from scipy import stats

df1=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
df4=pd.DataFrame()
df5=pd.DataFrame()
df6=pd.DataFrame()

# Graph generator:
G=nx.powerlaw_cluster_graph(8,5,0.3)

#Assign normally distributed weights to edges:
weights = np.random.normal(3, 1.5, nx.number_of_edges(G))
w = 0
for u, v, d in G.edges(data=True):
    d['weight'] = weights[w]
    w += 1

#Create list of source and sink nodes (Instances):
st_list = []

while len(st_list) != 5:
    st = [random.randint(0, len(G) - 1), random.randint(0, len(G) - 1)]
    if st[0] != st[1] and st not in st_list:
        st_list.append(st)

print("List of source and sink",st_list)

for k in range(5):
    #Maximum flow algorithm:
    flow_value,flow_dict = nx.maximum_flow(G, st_list[k][0], st_list[k][1], capacity='weight')
    #print(flow_dict)

    #Change edge colors
    edge_colors = ['black' if flow_dict[i][j] == 0 and flow_dict[j][i] == 0 else 'red' for i, j in G.edges()]

    #Change node properties:
    color_map = []
    node_sizes = []
    for node in G:
        if node == st_list[k][0]:
            color_map.append('skyblue')
            node_sizes.append(900)

        elif node == st_list[k][1]:
            color_map.append('orange')
            node_sizes.append(900)
        else:
            color_map.append('red')
            node_sizes.append(200)

    #Layout:
        pos = nx.fruchterman_reingold_layout(G, k=0.2, iterations=40)

    nx.draw(G, node_color=color_map, edge_color=edge_colors,
            node_size=node_sizes, width=weights, pos=pos,
            with_labels=True)
    plt.show()

    #Analysis of good targets and structural characteristics:
    fv_targets = {}
    for t in range(len(G)):
        if st_list[k][0] != t:

            #degree distribution
            st1 = time.time()
            flow_value = nx.maximum_flow_value(G, st_list[k][0], t, capacity='weight')
            fv_targets[t]=flow_value
            for c in range(30):
                for dd in range(100):
                    degree_distribution = nx.degree_centrality(G)
                e1 = time.time()
                execution_t1 = e1 - st1

                row = pd.DataFrame({'Structural_Characteristic': ['Degree Distribution'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t1,
                                    'Objective Value': flow_value})
                df1 = df1.append(row)


            #clustering coefficient
            st2 = time.time()
            for c in range(30):
                for clu in range(100):
                    clustering_coefficient = nx.clustering(G)
                e2 = time.time()
                execution_t2 = e2 - st2

                row = pd.DataFrame({'Structural_Characteristic': ['Clustering Coefficient'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t2,
                                    'Objective Value': flow_value})
                df2 = df2.append(row)

                #closeness centrality
            st3 = time.time()
            for c in range(30):
                for clo in range(100):
                    closeness_centrality = nx.closeness_centrality(G)
                e3 = time.time()
                execution_t3 = e3 - st3

                row = pd.DataFrame({'Structural_Characteristic': ['Closeness centrality'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t3,
                                    'Objective Value': flow_value})
                df3=df3.append(row)

                #load centrality
            st4 = time.time()
            for c in range(30):
                for lc in range(100):
                    load_centrality = nx.load_centrality(G)
                e4 = time.time()
                execution_t4 = e4 - st4
                row = pd.DataFrame({'Structural_Characteristic': ['Load Centrality'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t4,
                                    'Objective Value': flow_value})
                df4 = df4.append(row)

                #eccentricity
            st5 = time.time()
            for c in range(30):
                for e in range(100):
                    eccentricity = nx.eccentricity(G)
                e5 = time.time()
                execution_t5 = e5 - st5
                row = pd.DataFrame({'Structural_Characteristic': ['Eccentricity'],
                                    'Instance': k,
                                    'Target Node': t,
                                    'Time': execution_t5,
                                    'Objective Value': flow_value})
                df5=df5.append(row)

            #pagerank
            st6 = time.time()
            for c in range(30):
                for pr in range(100):
                    page_rank = nx.pagerank(G, alpha=0.95)
                e6 = time.time()
                execution_t6 = e6 - st6

                row = pd.DataFrame({'Structural_Characteristic': ['PageRank'],
                                    'Instance': k,
                                   'Target Node': t,
                                   'Time': execution_t6,
                                   'Objective Value': flow_value})
                df6 = df6.append(row)

    bt=heapq.nlargest(3, fv_targets, key=fv_targets.get)
    print('The best targets are:',bt)

    #Analysis of good sources:
    fv_sources = {}
    for s in range(len(G)):
        if s != st_list[k][1]:
            fv = nx.maximum_flow_value(G, s, st_list[k][1], capacity='weight')
            fv_sources[s] = fv

    bs = heapq.nlargest(3, fv_sources, key=fv_sources.get)
    print('The best sources are:',bs)

df1.to_csv('data1.csv',index=False)
df2.to_csv('data2.csv',index=False)
df3.to_csv('data3.csv',index=False)
df4.to_csv('data4.csv',index=False)
df5.to_csv('data5.csv',index=False)
df6.to_csv('data6.csv',index=False)

