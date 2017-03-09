'''
Created on 7 mar. 2017

@author: jorge
'''
import networkx as nx

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
    file=open(input,'r')
    out=open(output,'w')
    for line in file:
        aux=''
        data=line.split(',')
        for i in range(len(data)-1):
            aux+=str(data[i])+' &'
        aux+=str(data[i])+' \\\ \hline'
        out.write(aux+' \n')
    out.close()
    file.close()
    return 0
            
        
    