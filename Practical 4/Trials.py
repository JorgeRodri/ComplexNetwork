'''
Created on 6 jun. 2017

@author: jorge
'''
from functions.monteCarloSimulation import Simulation,get_stability
import networkx as nx
import time
from numpy import linspace
import pickle 
from os import walk
import matplotlib.pyplot as plt


def simulate(G, beta, mu, Nrep=50, ini_ro=0.2):
    n=0
    stability=0
    while n<Nrep:
        ro=Simulation(G, beta, mu, ro=ini_ro)
        stability+=get_stability(ro)
        n+=1
    return stability/Nrep

def get_values(G, betas, mu, ini_ro=0.2, Nrep=50):
    ros=[]
    for beta in betas:
        ro=simulate(G, beta, mu, Nrep=Nrep, ini_ro=ini_ro)
        ros.append(ro)
    return ros

path='Networks/'
save_path='Network_results/'

if __name__ == '__main__':
    betas= linspace(0,1,51)
    mu=0.4
    G=nx.read_pajek('Networks/ER500_03.net')
    print('\nSimulation for ER500_03.')
    t1=time.time()
    ros=get_values(G, betas, mu, Nrep=1)
    t2=time.time()
    print('End of the simulation.')
    print('Time: '+str(t2-t1))
    plt.plot(betas,ros,'o-')
    plt.show()
