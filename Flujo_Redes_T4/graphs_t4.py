import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from networkx.algorithms.flow import preflow_push
import time
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

all_data=pd.DataFrame()

def assign_normally_distributed_weight (mu,sigma,Graph_name):
    weights = np.random.normal(mu, sigma, nx.number_of_edges(Graph_name))
    k = 0
    for u, v, d in Graph_name.edges(data=True):
        d['weight'] = weights[k]
        k += 1

complete_graph_times = []
wheel_graph_times = []
star_graph_times = []

max_flow_times=[]
min_cut_times=[]
preflow_push_times=[]

number_of_nodes = []
for j in range(10):
    for i in range(2,6):
        i = 2 ** i
        number_of_nodes.append(i)

        #COMPLETE GRAPH
        start_C = time.time()
        C=nx.complete_graph(i)
        end_C = time.time()
        execution_time_C = end_C - start_C
        complete_graph_times.append(execution_time_C)

        assign_normally_distributed_weight(12,0.4,C)

        # WHEEL GRAPH
        start_W = time.time()
        W = nx.wheel_graph(i)
        end_W = time.time()
        execution_time_W = end_W - start_W
        wheel_graph_times.append(execution_time_W)

        assign_normally_distributed_weight(12, 0.4, W)

        # STAR GRAPH
        start_S = time.time()
        S = nx.star_graph(i)

        end_S = time.time()
        execution_time_S = end_S - start_S
        star_graph_times.append(execution_time_S)

        assign_normally_distributed_weight(12, 0.4, S)

        for p in range(5):
            #Generar pareja s-t
            ss_list = []

            while len(ss_list) != 5:
                source_and_sink = [random.randint(0, len(C) - 1), random.randint(0, len(C) - 1)]
                if source_and_sink[0] != source_and_sink[1] and source_and_sink not in ss_list:
                    ss_list.append(source_and_sink)

            #Maximum flow Complete Graph
            start_flow = time.time()
            for k in range(5):
                flow_value = nx.maximum_flow(C, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow

            row=pd.DataFrame({'Generator':['Complete_Graph'],
                               'Algorithm':['Maximum_Flow'],
                               'Order':i,
                               'Density':round(C.size() / nx.complete_graph(i).size(),2),
                               'Time':execution_time_flow + execution_time_C})
            all_data=all_data.append(row)


            #Minimum cut Complete Graph
            start_flow = time.time()
            for k in range(5):
                cut_value = nx.minimum_cut(C, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow

            row = pd.DataFrame({'Generator': ['Complete_Graph'],
                                'Algorithm': ['Minimum_Cut'],
                                'Order': i,
                                'Density': round(C.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_C})
            all_data = all_data.append(row)

            #Preflow push Complete Graph
            start_flow = time.time()
            for k in range(5):
                R = preflow_push(C, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow

            row = pd.DataFrame({'Generator': ['Complete_Graph'],
                                'Algorithm': ['Preflow_Push'],
                                'Order': i,
                                'Density': round(C.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_C})
            all_data = all_data.append(row)

            # Maximum flow Wheel Graph
            start_flow = time.time()
            for k in range(5):
                flow_value = nx.maximum_flow(W, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow


            row = pd.DataFrame({'Generator': ['Wheel_Graph'],
                                'Algorithm': ['Maximum_Flow'],
                                'Order': i,
                                'Density': round(W.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_W})
            all_data = all_data.append(row)

            # Minimum cut Wheel Graph
            start_flow = time.time()
            for k in range(5):
                cut_value = nx.minimum_cut(W, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow


            row = pd.DataFrame({'Generator': ['Wheel_Graph'],
                                'Algorithm': ['Minimum_Cut'],
                                'Order': i,
                                'Density': round(W.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_W})
            all_data = all_data.append(row)

            # Preflow push Wheel Graph
            start_flow = time.time()
            for k in range(5):
                R = preflow_push(W, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow
            row = pd.DataFrame({'Generator': ['Wheel_Graph'],
                                'Algorithm': ['Preflow_Push'],
                                'Order': i,
                                'Density': round(W.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_W})
            all_data = all_data.append(row)

            # Maximum flow Star Graph
            start_flow = time.time()
            for k in range(5):
                flow_value = nx.maximum_flow(S, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow

            row = pd.DataFrame({'Generator': ['Star_Graph'],
                                'Algorithm': ['Maximum_Flow'],
                                'Order': i,
                                'Density': round(S.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_S})
            all_data = all_data.append(row)

            # Minimum cut Star Graph
            start_flow = time.time()
            for k in range(5):
                cut_value = nx.minimum_cut(S, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow

            row = pd.DataFrame({'Generator': ['Star_Graph'],
                                'Algorithm': ['Minimum_Cut'],
                                'Order': i,
                                'Density': round(S.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_S})
            all_data = all_data.append(row)

            # Preflow push Star Graph
            start_flow = time.time()
            for k in range(5):
                R = preflow_push(S, ss_list[k][0], ss_list[k][1], capacity='weight')
            end_flow = time.time()
            execution_time_flow = end_flow - start_flow
            preflow_push_times.append(execution_time_flow)

            row = pd.DataFrame({'Generator': ['Star_Graph'],
                                'Algorithm': ['Preflow_Push'],
                                'Order': i,
                                'Density': round(S.size() / nx.complete_graph(i).size(),2),
                                'Time': execution_time_flow + execution_time_S})
            all_data = all_data.append(row)

print(all_data)

all_data.to_csv('data.csv',index=False)

sns.boxplot(x = 'Generator', y = 'Time', data = all_data)
plt.savefig("box_generator.eps")
plt.show()

sns.boxplot(x = 'Order', y = 'Time', data = all_data)
plt.savefig("box_order.eps")
plt.show()

sns.boxplot(x = 'Algorithm', y = 'Time', data = all_data)
plt.savefig("box_algorithm.eps")
plt.show()

sns.boxplot(x = 'Density', y = 'Time', data = all_data)
plt.savefig("box_density.eps")
plt.show()

model= ols('Time ~ Generator + Order + Algorithm + Density + Generator*Order + Generator*Algorithm + Generator*Density + Order*Algorithm + Order*Density + Algorithm*Density',\
           data=all_data).fit()

ANOVA = sm.stats.anova_lm(model, typ=2)
print(ANOVA)

for i in range(len(ANOVA)):
    print("{:s} {:s}is significative".format(ANOVA.index[i], "" if ANOVA['PR(>F)'][i] < 0.05 else "It is not "))