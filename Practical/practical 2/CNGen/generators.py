import random
import networkx as nx
import numpy as np
from functions import truncated_power_law


def GetDegreeDist(n, DegreeDistribution, val):
    
    if DegreeDistribution=="Poisson":       #
        v=np.random.poisson(val, n)         #                   #
    elif DegreeDistribution=="PowerLaw":    #Poner en una funcion
        d = truncated_power_law(val)        
        v = d.rvs(size=n)                   #                                #
    else:                                   #
        raise "Wrong Degree Distribution."  #
    if sum(v)%2!=0:                     #
            v[0]=v[0]+1 
    return v

def getCMedges(dd,nodes):
    stublist=[]
    for n in nodes:
        for i in range(dd[n-1]):
            stublist.append(n)
    random.shuffle(stublist)
    edges=[]
    while stublist:
        n1=stublist.pop()
        n2=stublist.pop()
        edges.append((n1,n2))
    return edges
    
def add_barabasi_node(G,node,m):
    i=0
    while i<m:
        degrees=G.degree().values()
        prob=[float(degrees[index])/sum(degrees) for index in range(len(degrees))]
        candidate=np.random.choice(G.nodes(),p=prob)
        G.add_edge(node,candidate)
        i+=1
    return G
 
def create_clique(m):
    nodes=list(range(1,m+1))
    G=nx.Graph()
    G.add_nodes_from(nodes)
    for i in range(m):
        for j in range(m):
            if i!=j : G.add_edge(nodes[i],nodes[j])
    return G

def rewire(G,edge):
    nodes=G.nodes()
    G.remove_edge(*edge)
    i=edge[0]
    wired=False
    while not wired:
        candidate=random.choice(nodes)
        if candidate!=i and (i,candidate) not in G.edges() and (candidate,i) not in G.edges():
            G.add_edge(i,candidate)
            wired=True
    return(G)

def GenER(n,p):
    G=nx.Graph()
    nodes=list(range(1,n+1))
    G.add_nodes_from(nodes)
    for i in range(n):
        for j in range(n-i):
            if random.random()<p: G.add_edge(nodes[i],nodes[n-j-1])
    return G
                
def GenWS(n,k,p):
    G=nx.MultiGraph()
    #creating the ring
    nodes=list(range(1,n+1))
    G.add_nodes_from(nodes)
    for i in range(n):
        for j in range(1,(k+1)/2):
            G.add_edge(nodes[i],nodes[i-j])
            G.add_edge(nodes[i],nodes[i-j-1])
    #rewiring
    edges=nx.edges(G)
    for edge in edges:
        if random.random()<p:
            G=rewire(G,edge)    
    return G

def GenBA(n,m):
    G=create_clique(5) if m<5 else create_clique(2*m) 
    nodes=list(range(6,n+1))
    for node in nodes:
        G=add_barabasi_node(G,node,m)
    return G

def GenCM(n,DegreeDistribution="Poisson", val=2, MultiGraph=True):
    if MultiGraph: 
        G=nx.MultiGraph() 
    else: 
        G=nx.Graph()
        
    nodes=list(range(1,n+1))
    v=GetDegreeDist(n, DegreeDistribution, val)
    edges=getCMedges(v,nodes)   
    G.add_edges_from(edges)
    return G