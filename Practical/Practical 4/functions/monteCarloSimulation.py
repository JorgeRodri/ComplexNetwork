'''
Created on 25 may. 2017

@author: jorge
'''
import random
from numpy import mean

def Simulation(G, beta, mu, Nrep=100, ro=0.2, Tmax=1000, Ttrans=900):
    step=0
    ros=[]
    nodes=G.nodes()
    infected=[x for x in nodes if random.random()<ro]
    susceptible=[x for x in nodes if x not in infected]
    while step<Tmax:
        recover=[]
        infect=[]
        step+=1
        for node in infected:
            if random.random()<mu:
                recover.append(node)
        for node in susceptible:
            for i in G.neighbors(node):
                if i in infected and random.random()<beta:
                    infect.append(node)
                    break
        for i in infect:
            susceptible.remove(i)
            infected.append(i)
        for i in recover:
            infected.remove(i)
            susceptible.append(i)
        if step>Ttrans:
            ros.append(float(len(infected))/float(len(nodes)))
            
    return ros

def get_stability(ro):
    if ro[-1]==0:
        stable=0
    else:
        stable=mean(ro)
    return stable