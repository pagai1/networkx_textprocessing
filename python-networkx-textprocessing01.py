#!/usr/bin/python
import networkx as nx
import matplotlib.pyplot as plt
import time
import sys
import json
import csv

from builtins import len
from networkx.algorithms.coloring.greedy_coloring_with_interchange import Node
from networkx.classes.function import get_node_attributes
from networkx.readwrite import json_graph
from _operator import itemgetter
from xlwt.ExcelFormulaLexer import false_pattern
from operator import __truediv__


# General functionality
def to_ms(time):
    return ("%.3f" % time)

def import_node_link_data_to_graph(inputfile):
    file_to_read = open(inputfile, 'r')
    json_data = json.loads(file_to_read.read())    
    return json_graph.node_link_graph(json_data, directed=True, multigraph=False)

def export_graph_to_node_link_data(G,outputfile):
    print("Exporting graph to node_link_data-file")
    file_to_write = open(outputfile, 'w')
    file_to_write.write(json.dumps(json_graph.node_link_data(G)))

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


# Algorithms
def get_hits(G):
    hubs_auths = {}
    algoTime=time.time() 
    peng = nx.hits(G,max_iter=100,normalized=True)
    print("RUNTIME Hits - " +  str(len(G.nodes())) + " entries - " + to_ms((time.time() - algoTime)) + "s.")   
    for dings in peng:
        for bums in dict(sorted(dings.items(),key=lambda item: item[1])):
            print(bums,dings[bums],G.nodes[bums]['name'])
#    for bums in nx.hits(G,max_iter=500,normalized=True):
#        for bla in bums:
#            print(str(bla))

def algo_betweenness_centrality(G):
#    actor_list=[x for x,y in G.nodes(data=True) if y['type'] == 'actor']
#    subG = G.subgraph(actor_list)
    dict_nodes = []
    algoTime=time.time()    
    dict_nodes = nx.betweenness_centrality(G,normalized=False, endpoints=False);
    print("RUNTIME BetweennessCentrality - " +  str(len(G.nodes())) + " entries - " + to_ms((time.time() - algoTime)) + "s.")   
    print("Result:")
    for bums in dict(sorted(dict_nodes.items(), key=lambda item: item[1])):
        print(bums,dict_nodes[bums],G.nodes[bums]['name'])
#    print("RUNTIME ClosenessCentrality - " +  str(limit) + " entries - " + str(len(actor_list)) + " actors : " + to_ms((time.time() - algoTime)) + "s.")


def algo_shortest_path(G):
    actor_list=[x for x,y in G.nodes(data=True) if y['type'] == 'actor']
    subG = G.subgraph(actor_list)
    print("Example: Calculating shortest path from anyone to Brad Pitt")
    start_time=time.time()
    for actor in actor_list:
        try:
            path = nx.shortest_path(subG, source=(actor), target='Brad Pitt')
        except nx.NetworkXNoPath as e:
            path = e
        except nx.NodeNotFound as e:
            path = e
    #     print(path)
    end_time=time.time()
    print("RUNTIME ShortestPath: " + str(end_time - start_time) )

def algo_pagerank(G):
    print("Calculating pagerank")
    actor_list=[x for x,y in G.nodes(data=True) if y['type'] == 'actor']
    subG = G.subgraph(actor_list)
    start_time = time.time()
    calculation = nx.pagerank(subG, alpha=0.85, weight='count', tol=1e-10)
    end_time = time.time()
    print("Result:")
    for bums in dict(sorted(calculation.items(), key=lambda item: item[1])):
        print(bums)
    print("RUNTIME PageRank: ", end_time - start_time)


def create_graph_from_neo4j_csv(G,filePath):
    with open(filePath,'r') as csv_file:
        reader = csv.DictReader(csv_file,quotechar = '"', delimiter=',')
        for line in reader:
            if line['_id'] != "":
                G.add_node(line['_id'], weight=line['occur'], label=line['_labels'], name=line['name'])
            else:
                G.add_edge(line['_start'],line['_end'],type=line['_type'],cost=line['cost'],count=['count'],dice=['dice'])
                G.add_edge(line['_end'],line['_start'],type=line['_type'],cost=line['cost'],count=['count'],dice=['dice']) 
 
    start_time = time.time() 
    dict_nodes = nx.closeness_centrality(G)
    print("ZEIT: " + str(time.time() - start_time))
    #print(G.nodes(data=True)) 

    #for bums in dict(sorted(dict_nodes.items(), key=lambda item: item[1])):
    #    print(bums,dict_nodes[bums],G.nodes[bums]['name'])
         
G = nx.Graph()
filePath='/home/pagai/graph-data/cooccsdatabase/cooccsdb.csv'

# Loading headers
header_reader = csv.reader(filePath)
print("HEADERS : " + str(get_column_names(header_reader)))

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
#algo_shortest_path(G)
#algo_pagerank(G)
#algo_betweenness_centrality(G)
get_hits(G)

draw_graph(G)


#print(pagerank_scipy(subG))
#if limit < 50:
#    draw_graph(subG)
#print("FERTIG")
