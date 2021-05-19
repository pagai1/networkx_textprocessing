'''
Created on 17.05.2021

@author: pagai
'''
import networkx as nx
import time
from algoPackage.helpers import to_ms

def algo_pagerank(G):
    start_time = time.time()
    calculation = nx.pagerank(G, alpha=0.85, max_iter=25, weight='cost')
    print("TIME: " + to_ms(time.time() - start_time) + " s.")
    #calculation = nx.pagerank_numpy(G, alpha=0.85, weight='count')
    #calculation = nx.pagerank_scipy(G, alpha=0.85, max_iter=25)
    i=0
    end_time = time.time()
    print("Result:")
    for node in dict(sorted(calculation.items(), key=lambda item: item[1], reverse=True)):
        i += 1
        if i > 25:
            break
        print(calculation[node],G.nodes[node]['name'])
    print("RUNTIME PageRank: ", end_time - start_time)
