# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 16:07:05 2017

Generates the values for the tables asked for this exercise
@author: jorge
"""


path='A1-networks/'

import numpy as np
import networkx as nx
from utils import *

files=['toy/circle9.net', 'toy/star.net', 'toy/graph3+1+3.net', 'toy/grid-p-6x6.net', 'model/homorand_N1000_K4_0.net', 'model/ER1000k8.net', 'model/SF_1000_g2.7.net', 'model/ws1000.net', 'real/zachary_unwh.net', 'real/airports_UW.net']
results=[]

file_name= 'toy/rb25.net'
for i in files:
    
    G=nx.read_pajek(path+i)
    
    print('\n\ndatabase: '+i)
    #print(G.nodes())
    #print(G.edges())
    
    
    numbNodes=G.number_of_nodes()
    numbEdges=G.number_of_edges()
    
    print('Number of nodes: ' + str(numbNodes))
    print('Number of edges: ' + str(numbEdges))
    
    degrees=nx.degree(G).values()
    
    print('Degree in formation: ' + 'Mean: ' + str(np.mean(degrees)) + ', Maximum: '+ str(max(degrees))  +' and Minimum: '+ str(min(degrees)))
    
    clustering=nx.clustering(nx.Graph(G)).values()
    print('Average clustering coefficient: ' + str(np.mean(clustering)))
    
    assortativity=nx.degree_assortativity_coefficient(G)
    #assortativity=nx.numeric_assortativity_coefficient(G)
    
    print('Assortativity: '+str(assortativity))
    
    average_path, diameter = average_path_calculation(G)
    print('Average path length: '+str(average_path)+ '\nDiameter: '+str(diameter))
    data_results=(i, numbNodes, numbEdges, np.mean(degrees), max(degrees), min(degrees), np.mean(clustering), assortativity, average_path, diameter)
    results.append(data_results)
    
file=open('results.txt', 'w')
for i in results:
    for j in i:
        file.write(str(j)+',')
    file.write('\n')
file.close()

convert_to_table('results.txt', 'table.txt')