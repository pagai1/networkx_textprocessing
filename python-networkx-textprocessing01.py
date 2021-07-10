#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt
import time
import json

#from algoPackage.pageRank import algo_pagerank
#from algoPackage.hits import get_hits
#from algoPackage.betweenness_centrality import algo_betweenness_centrality 
#from algoPackage.shortestPath import all_algo_shortest_path,algo_shortest_path
#from helpers.networkx_load_n_save import *
#from helpers.generalStuff import *

# import own helper-modules
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__),"../../networkx_modules")))
from helpers.generalStuff import *
from helpers.networkx_load_n_save import *
from helpers.search_functions import *
from algoPackage.pageRank import *
from algoPackage.simRank import *
from algoPackage.hits import *
from algoPackage.shortestPath import *
from algoPackage.jaccard_coefficient import *
from algoPackage.degree_centrality import *

from builtins import len
from networkx.algorithms.coloring.greedy_coloring_with_interchange import Node
from networkx.classes.function import get_node_attributes
from networkx.readwrite import json_graph
from _operator import itemgetter
from xlwt.ExcelFormulaLexer import false_pattern
from operator import __truediv__

# General functionality

def get_column_names(filereader):
  headers = next(filereader, None)
  return headers

def remove_doubles(inputlist):
    return list(set(inputlist))

# Draw the graph
def draw_graph(Graph):
    #pos = nx.spring_layout(G)
#    nx.draw(G, pos)
    node_label = nx.get_node_attributes(G, 'name')
    edge_label = nx.get_edge_attributes(G, 'count')
    nx.draw_kamada_kawai(Graph,with_labels=True,labels=node_label)
    nx.draw_circular(Graph,with_labels=True,labels=node_label)
#    nx.draw(Graph,with_labels=False)
#    node_labels = nx.get_node_attributes(G, 'name')
#    nx.draw_networkx_labels(G, pos=nx.spring_layout(G), labels = node_labels)
#    edge_labels = nx.get_edge_attributes(G,"_type")
#   
#    nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels = edge_labels)
#    pos = nx.spring_layout(G)
#    nx.draw_kamada_kawai(Graph,with_labels=True)
#    node_labels = nx.get_node_attributes(G,'name')
#    nx.draw_networkx_labels(G, pos, labels = node_labels)
#    edge_labels = nx.get_edge_attributes(G,'type')
#    nx.draw_networkx_edge_labels(G, pos, labels = edge_labels)
    plt.plot()
    plt.show()


         
G = nx.Graph()
filePath='/home/pagai/graph-data/cooccsdatabase/cooccsdb.csv'

create_graph_from_neo4j_csv(G, filePath)

#### IMPORT FILE
#start_time = time.time()
#G = import_node_link_data_to_graph('/tmp/node_link_data.json')
#print("File load finished in " + str(time.time() - start_time))

# EXPORT FILE
#start_time = time.time()
#export_graph_to_node_link_data(G, '/tmp/node_link_data_5000.json')
#print("File export finished in : " + str(time.time() - start_time))


# ALGOS
# algo_shortest_path(G)
# all_algo_shortest_path(G,forceSubGraphCreation=True,nodeType='SINGLE_NODE')
# all_algo_shortest_path(G,nodeType='SINGLE_NODE')
# algo_pagerank(G)
# algo_betweenness_centrality(G)
# get_hits(G)

