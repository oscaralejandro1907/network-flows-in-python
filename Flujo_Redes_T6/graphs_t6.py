import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sns

# Graph generator:
G=nx.balanced_tree(3,4)

n_nodes=len(G)
n_edges=nx.number_of_edges(G)

print("Number of nodes:",n_nodes)
print("Number of edges:",n_edges)

#Assign normally distributed weights to edges:
weights = np.random.normal(3, 0.5, nx.number_of_edges(G))
w = 0
for u, v, d in G.edges(data=True):
    d['weight'] = weights[w]
    w += 1

#Change node properties:
color_map = []
node_sizes = []
for node in G:
    if node == 0:
        color_map.append('skyblue')
        node_sizes.append(900)
    else:
        color_map.append('red')
        node_sizes.append(200)

#Minimum cut algorithm:
cut_value, partition=nx.minimum_cut(G,0,len(G)-1,capacity='weight')
print(cut_value)
print(partition)

#Layout:
pos = nx.kamada_kawai_layout(G)

nx.draw(G, node_color=color_map,
        node_size=node_sizes, width=weights, pos=pos,
        with_labels=True)
#plt.savefig("Graph1.eps", format="EPS")

plt.show()

#Data for statistical analysis

all_data=pd.DataFrame()

cluster1=[1,4,13,40,41,42,45,14,43,44,15,46,47,48,5,16,49,50,51,17,54,52,53,18,55,53,56,57,6,19,
          59,58,60,20,61,62,63,21,64,66,65]

cluster2=[2,7,22,67,68,69,23,70,71,72,24,73,74,75,8,25,76,78,77,26,80,79,27,81,82,83,84,9,28,85,
          86,87,29,88,89,90,30,93,92,91]

cluster3=[3,12,38,117,115,116,39,118,119,120,37,114,112,113,36,111,110,109,11,34,104,105,103,
          35,106,107,108,10,32,97,98,99,31,100,101,102,94,95,96]

c1_values=[]
c2_values=[]
c3_values=[]

# Analysis for Cluster 1:
for i in cluster1:
    #Maximum flow algorithm:
    flow_value,flow_dict = nx.maximum_flow(G, 0, i, capacity='weight')
    c1_values.append(flow_value)

    df=pd.DataFrame({'Cluster':[1],
                    'Flow_Value':flow_value})

    all_data=all_data.append(df)

mean=np.mean(c1_values)
std_dev=np.std(c1_values)

normality_test=stats.shapiro(c1_values)

print("Mean for Cluster 1:",mean)
print("Standard deviation for Cluster 1:",std_dev)
print("Normality test for Cluster 1:",normality_test,"\n")

#Histogram for cluster 1:
hist, bin_edges=np.histogram(c1_values,density=True)
first_edge, last_edge = np.min(c1_values),np.max(c1_values)

n_equal_bins = 15
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(c1_values,bins=bin_edges,rwidth=0.75)
plt.xlabel('Flow values')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig("Histogram_Cluster1.eps", format="EPS")
plt.show(1)

# Analysis for Cluster 2:
for j in cluster2:
    # Maximum flow algorithm:
    flow_value, flow_dict = nx.maximum_flow(G, 0, j, capacity='weight')
    c2_values.append(flow_value)

    df = pd.DataFrame({'Cluster': [2],
                       'Flow_Value': flow_value})

    all_data = all_data.append(df)

mean=np.mean(c2_values)
std_dev=np.std(c2_values)

normality_test=stats.shapiro(c2_values)

print("Mean for Cluster 2:",mean)
print("Standard deviation for Cluster 2:",std_dev)
print("Normality test for Cluster 2:",normality_test,"\n")

#Histogram of Cluster 2
hist, bin_edges=np.histogram(c2_values,density=True)
first_edge, last_edge = np.min(c2_values),np.max(c2_values)

n_equal_bins = 15
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(c1_values,bins=bin_edges,rwidth=0.75)
plt.xlabel('Flow values')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig("Histogram_Cluster2.eps", format="EPS")
plt.show(2)

#Analysis for Cluster 3:
for k in cluster3:
    # Maximum flow algorithm:
    flow_value, flow_dict = nx.maximum_flow(G, 0, k, capacity='weight')
    c3_values.append(flow_value)

    df = pd.DataFrame({'Cluster': [3],
                       'Flow_Value': flow_value})

    all_data = all_data.append(df)

mean=np.mean(c3_values)
std_dev=np.std(c3_values)

normality_test=stats.shapiro(c3_values)

print("Mean for Cluster 3:",mean)
print("Standard deviation for Cluster 3:",std_dev)
print("Normality test for Cluster 3:",normality_test,"\n")

#Histogram of Cluster 3
hist, bin_edges=np.histogram(c3_values,density=True)
first_edge, last_edge = np.min(c3_values),np.max(c3_values)

n_equal_bins = 15
bin_edges = np.linspace(start=first_edge, stop=last_edge,num=n_equal_bins + 1, endpoint=True)

plt.hist(c3_values,bins=bin_edges,rwidth=0.75)
plt.xlabel('Flow values')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig("Histogram_Cluster3.eps", format="EPS")
plt.show(3)

sns.boxplot(x = 'Cluster', y = 'Flow_Value', data = all_data)
plt.savefig("boxplot_flow_value.eps")
plt.show()

all_data.to_csv('data.csv',index=False)