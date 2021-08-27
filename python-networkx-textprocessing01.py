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

filePath='/home/pagai/graph-data/cooccsdatabase/cooccsdb.csv'
verbose=False
doExport=True
createByImport=False
doAlgo=False
algoVerbose=False
deleteTest=False

importExportFileName = "/tmp/node_link_data_export_cooccsdb.json"

startTime = time.time()
G = create_graph_from_neo4j_csv(filePath, inputDirectedData=True, outputDirectedGraph=True)
if verbose:
    print(nx.info(G))

############ Export/Import ##########
if createByImport:
    importFile='/tmp/node_link_data_export_cooccs.json'
    print("IMPORTING " + importFile)
    start_time = time.time()
    G = import_node_link_data_to_graph(importFile, verbose=verbose)
    if (verbose): 
        print("IMPORTED FILE: " + importFile)
        print(nx.info(G))

if doExport:
    export_graph_to_node_link_data(G, '/tmp/node_link_data_export_cooccs.json', verbose=verbose)
endTime = time.time()
print(G.number_of_nodes(), G.number_of_edges(), to_ms(endTime - startTime), sep=",")

########## DELETE-test Clear ################
if deleteTest:
    numberOfNodes = G.number_of_nodes()
    numberOfEdges = G.number_of_edges()
    export_graph_to_node_link_data(G, importExportFileName+"_full", verbose=verbose)
    
    start_time_clear=time.time()
    G.clear()
    export_graph_to_node_link_data(G, importExportFileName, verbose=verbose)
    end_time_clear=time.time()
    print(numberOfNodes, numberOfEdges, to_ms(end_time_clear - start_time_clear), sep=",")

############ ALGOS #############
if doAlgo:

    #algo_shortest_path(G)
    #algo_all_pairs_dijkstra(G,verbose=True,inputWeight='weight')
    #algo_all_pairs_bellman_ford_path(G,verbose=True,inputWeight='weight')
    
    #all_pairs_shortest_path(G)
    
    #### PAGERANK
    weightInputForAlgos="weight"
    #weightInputForAlgos=None
    
    print("==============================")
    #algo_pagerank(G, "default",  weightInput=weightInputForAlgos, verbose=algoVerbose, maxLineOutput=15)
    # NUMPY IS OBSOLETE
    #algo_pagerank(G, "numpy", weightInput=weightInputForAlgos, verbose=algoVerbose, maxLineOutput=10)
    algo_pagerank(G, "scipy", weightInput=weightInputForAlgos, verbose=algoVerbose, maxLineOutput=0)
    print("==============================")
    print("EXECUTION TOOK: " + to_ms(time.time() - start_time))
    
    
    #### SIMRANK
    #algo_simRank(G,verbose=True,max_iterations=1)
    #algo_degree_centrality(G, verbose=True)
    #algo_all_pairs_shortest_path(G,verbose=False,inputWeight='weight')
    
    #### OWN DEGREE CENTRALITY
    #peng = sorted(G.degree, key=lambda x: x[1], reverse=True)
    #if (verbose):
    #    for bums in peng:
    #        print(bums)
    
    
    #algo_degree_centrality(G, verbose=False)
    
    
    #print("TIME: " + to_ms(end_time - start_time))
    
        
    #print(str(G.number_of_nodes()) + "," + str(G.number_of_edges()) + "," + to_ms(end_time-start_time))
    #algo_jaccard_coefficient(G,G.edges(),verbose=True) 
    
    #get_hits(G)
    #draw_all_shortest_path_for_single_node(G,"1")
    #all_shortest_path_for_single_node(G,"12")





