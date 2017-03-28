import random
import networkx as nx
import numpy as np

'''
class CNgenerator(nx):
    
    def __init__(self, graphType, prob):
        self.t=graphType
        self.p=prob
 pass
 '''
 
def add_barabasi_node(G,node,m):
    i=0
    while i<m:
        degrees=G.degree().values()
        prob=[float(degrees[index])/sum(degrees) for index in range(len(degrees))]
        candidate=np.random.choice(G.nodes(),p=prob)
        if candidate!=i and (node,candidate) not in G.edges() and (candidate,node) not in G.edges():
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
    G=nx.Graph()
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