'''
Created on 7 mar. 2017

Generates the histograms needed in the task
@author: jorge
'''
from utils import histogram
import networkx as nx
import matplotlib.pyplot as plt

path='A1-networks/'
files=['model/ER1000k8.net', 'model/SF_1000_g2.7.net', 'model/ws1000.net', 'real/airports_UW.net']
names=['ER1000k8', 'SF_1000_g2.7', 'ws1000', 'airports_UW']

for i in range(len(files)):
    G=nx.read_pajek(path+files[i])
    plt=histogram(G, log=True, norm=True, n=10)
    plt.title('Log histogram for '+names[i])
    plt.savefig('log_'+names[i]+'.png')
    plt.clf()
    plt=histogram(G, log=False, norm=True, n=10)
    plt.title('Normed histogram for '+ names[i])
    plt.savefig('norm_'+names[i]+'.png')
    plt.clf()
    plt=histogram(G, log=True, norm=True,cumu=-1, n=10)
    plt.title('Cumulative log histogram for '+names[i])
    plt.savefig('Cumu_log_'+names[i]+'.png')
    plt.clf()
    plt=histogram(G, log=False, norm=True,cumu=-1, n=10)
    plt.title('Cumulative normed histogram for '+ names[i])
    plt.savefig('Cumu_norm_'+names[i]+'.png')
    plt.clf()