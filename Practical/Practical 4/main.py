'''
Created on 25 may. 2017

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
'''
First experiments with an Erdos Redill model with 0.4 time=8,67
for an ER of 0.2 time 4.96

This has to be done for 50 betas
time would be 450 for 1st and 250 for second, which aceptable.

Time for the ER with 500 averaging 50 times the stable points time and for all the betas:
'''
path='Networks/'
save_path='Network_results/'

#falta el experimento con ER500 y ro_ini=0.5,1

if __name__ == '__main__':
    '''file_names=[]
    lstDir=walk(path)
    for (root, dirs, fil) in lstDir:
        for f in fil:
            file_names+=[f]
            
    for network in file_names:
        betas= linspace(0,1,51)
        mu=1
        if 'airports' not in network and 'CSphd' not in network:
            Nrep=10 
            G=nx.read_pajek(path+network)
            print('\nSimulation for '+network)
            t1=time.time()
            ros=get_values(G, betas, mu, Nrep=Nrep)
            t2=time.time()
            print('End of the simulation.')
            print('Time: '+str(t2-t1))
            with open(save_path+network[0:-4]+'_mu1_results.txt','wb') as f:
                pickle.dump(ros, f)'''
    #to do
    

    network='BA1000_2.net'
    betas= linspace(0,1,51)
    ro_ini=1
    mu=0.1
    Nrep=5
    G=nx.read_pajek(path+network)
    print('\nSimulation for '+network)
    t1=time.time()
    ros=get_values(G, betas, mu, Nrep=Nrep, ini_ro=ro_ini)
    t2=time.time()
    print('End of the simulation.')
    print('Time: '+str(t2-t1))
    with open(save_path+network[0:-4]+'mulow'+'_results.txt','wb') as f:
            pickle.dump(ros, f)          
    plt.plot(betas,ros,'o-')
    plt.xlabel('Betas')
    plt.ylabel('p')
    plt.title('p Changes over Beta')
    plt.savefig('figures/'+network[0:-4]+'.jpg')
    plt.show()           
                
