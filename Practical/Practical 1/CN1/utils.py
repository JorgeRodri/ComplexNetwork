'''
Created on 7 mar. 2017

@author: jorge
'''
import networkx as nx
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


def degree_counts(G):
    degrees = Counter(G.degree().values())
    return degrees

def degree_distribution(G):
    distribution=dict()
    degrees = Counter(G.degree().values())
    total=float(sum(degrees.values()))
    for i in degrees.keys():
        distribution[i]=float(degrees[i])/total
    return degrees, distribution

def average_path_calculation(G):
    nodes1=G.nodes()
    nodes2=G.nodes()
    N=len(nodes1)*(len(nodes1)-1)/2
    aux=0
    diameter=0
    for i in nodes1:
        nodes2.remove(i)
        for j in nodes2:
            path=nx.shortest_path(G,i,j)
            aux+=len(path)
            if diameter<len(path):
                diameter=len(path)
    return aux/N, diameter
     
def convert_to_table(input, output):
    f=open(input,'r')
    out=open(output,'w')
    for line in f:
        aux=''
        data=line.split(',')
        for i in range(len(data)-2):
            aux+=str(data[i])+' &'
        aux+=str(data[i])+' \\\ \hline'
        out.write(aux+' \n')
    out.close()
    f.close()
    return 0
            
def get_stats(files, path=''):
    results=[]
    for i in files:
    
        G=nx.read_pajek(path+i)
        
        numbNodes=G.number_of_nodes()
        numbEdges=G.number_of_edges()
        
        degrees=nx.degree(G).values()
                
        clustering=nx.clustering(nx.Graph(G)).values()
        
        assortativity=nx.degree_assortativity_coefficient(G)
                
        average_path, diameter = average_path_calculation(G)
        data_results=(i, numbNodes, numbEdges, np.mean(degrees), max(degrees), min(degrees), np.mean(clustering), assortativity, average_path, diameter)
        results.append(data_results)
        print i + ' done'
    return results

def print_stats(files, path=''):
    results=[]
    for i in files:
    
        G=nx.read_pajek(path+i)
        
        print('\n\ndatabase: '+i)
        
        numbNodes=G.number_of_nodes()
        numbEdges=G.number_of_edges()
        
        print('Number of nodes: ' + str(numbNodes))
        print('Number of edges: ' + str(numbEdges))
        
        degrees=nx.degree(G).values()
        
        print('Degree in formation: ' + 'Mean: ' + str(np.mean(degrees)) + ', Maximum: '+ str(max(degrees))  +' and Minimum: '+ str(min(degrees)))
        
        clustering=nx.clustering(nx.Graph(G)).values()
        print('Average clustering coefficient: ' + str(np.mean(clustering)))
        
        assortativity=nx.degree_assortativity_coefficient(G)        
        print('Assortativity: '+str(assortativity))
        
        average_path, diameter = average_path_calculation(G)
        print('Average path length: '+str(average_path)+ '\nDiameter: '+str(diameter))
        
        data_results=(i, numbNodes, numbEdges, np.mean(degrees), max(degrees), min(degrees), np.mean(clustering), assortativity, average_path, diameter)
        results.append(data_results)
        return results

def histogram(G, log=False, norm=False,cumu=0, n=10):
    degrees=G.degree().values()
    if log:
        plt.title("Log Histogram.")
        logbins = np.logspace(np.log10(min(degrees)), np.log10(max(degrees)), n)
        plt.hist(degrees, bins = logbins, cumulative=cumu, normed=norm)
        plt.gca().set_xscale('log')
        plt.gca().set_yscale('log')
        #plt.show()
    else:  
        plt.hist(degrees, n,cumulative=cumu, normed=norm)  # plt.hist passes it's arguments to np.histogram
        plt.title("Histogram without log.")
        #plt.show()
    return plt

