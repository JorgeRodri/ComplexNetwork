'''
Created on 5 jun. 2017

@author: jorge

Script for generating the networks and saving them
'''
import numpy as np

def print_stats(G):

    numbNodes=G.number_of_nodes()
    numbEdges=G.number_of_edges()
        
    print('Number of nodes: ' + str(numbNodes))
    print('Number of edges: ' + str(numbEdges))
        
    degrees=nx.degree(G).values()
        
    print('Degree information: ' + 'Mean: ' + str(np.mean(degrees)) + ', Maximum: '+ str(max(degrees))  +' and Minimum: '+ str(min(degrees)))
        
    data_results=(numbNodes, numbEdges, np.mean(degrees), max(degrees), min(degrees))
    return data_results, degrees
    
import networkx as nx

path='Networks/'
if __name__ == '__main__':
    s=7 #we fix a seed to obtain consistent results
    G1=nx.barabasi_albert_graph(1000, 2, seed=s)
    G20=nx.read_pajek('Networks/CSphd.net')
    G21=nx.read_pajek('Networks/airports_UW.net')
    G3=nx.erdos_renyi_graph(500, 0.03, seed=s)
    G4=nx.erdos_renyi_graph(1000, 0.03, seed=s)
    
    #print information about the obtained graphs
    print '\nStats for BA:'
    data_results1, degrees1 = print_stats(G1)
    print '\nStats for CSphd'
    data_results2, degrees2 = print_stats(G20)
    print '\nStats for Airports'
    data_results2, degrees2 = print_stats(G21)
    print '\nStats for ER 500'
    data_results3, degrees3 = print_stats(G3)
    print '\nStats for ER 1000'
    data_results4, degrees4 = print_stats(G4)
    
    nx.write_pajek(G1,path+'BA1000_2.net')
    nx.write_pajek(G3,path+'ER500_03.net')
    nx.write_pajek(G4,path+'ER1000_03.net')
