'''
Created on 16 abr. 2017

@author: jorge
'''
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def histogram(G, log=False, norm=False,cumu=0, n=10):
    degrees=G.degree().values()
    if log:
        plt.title("Log Histogram.")
        logbins = np.logspace(np.log10(min(degrees)), np.log10(max(degrees)), n)
        plt.hist(degrees, alpha=0.5, bins = logbins, cumulative=cumu, normed=norm,range=[min(G.degree().values()),max(G.degree().values())])
        plt.gca().set_xscale('log')
        plt.gca().set_yscale('log')
        #plt.show()
    else:  
        plt.hist(degrees, n,cumulative=cumu, alpha=0.5, normed=norm)  # plt.hist passes it's arguments to np.histogram
        plt.title("Histogram without log.")
        #plt.show()
    return plt

def powerlaw(G):
    degree=G.degree().values()
    n=len(degree)
    aux=[float(degree[i])/(float(min(degree))-0.5) for i in range(n)]
    alfa=1+ n* (sum(np.log(aux)))**(-1)
    return alfa

def truncated_power_law(a, m=50):
    x = np.arange(1, m+1, dtype='float')
    pmf = 1/x**a
    pmf /= pmf.sum()
    return stats.rv_discrete(values=(range(1, m+1), pmf))

