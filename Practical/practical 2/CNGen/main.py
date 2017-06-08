'''
Created on 22 mar. 2017

@author: jorge
'''

from generators import GenER, GenWS, GenBA, GenCM, GetDegreeDist
from functions import histogram, powerlaw
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

'''
G=GenER(100,0.1)

nx.draw(G)
plt.show()


G=GenWS(100,4,0.1)

nx.draw(G)
plt.show()


G=GenBA(1000,3)

gamma=powerlaw(G)
print gamma

nx.draw(G)
plt.show()

n=1000
#DD="Poisson"
DD="PowerLaw"
val=3

G=GenCM(n,DD, val, True)
v=GetDegreeDist(1000000, DD, val)
gamma=powerlaw(G)

print gamma

plt2=histogram(G, log=False, norm=True, cumu=0, n=16)
plt2.hist(v,16,cumulative=0, alpha=0.5, normed=True, range=[1,max(G.degree().values())])

plt2.show()
'''
#generate networks
'''
path="networks/"

for n in [50, 100, 500, 1000]:
    for i in [0.00,0.01,0.02, 0.05, 0.1]:
        G=GenER(n,i)
        nx.write_pajek(G,path+"ER/GenNetwork, n="+str(n)+", p="+str(i).replace(".",",")+".net")
    print "ER done for n="+str(n)
    
    for i in [0.00,0.1,0.2, 0.5, 0.9, 1.0]:
        G=GenWS(n,4,i)
        nx.write_pajek(G,path+"WS/GenNetwork, n="+str(n)+" k=4 p="+str(i).replace(".",",")+".net")
    print "WS done for n="+str(n)
    
    for i in [1,2,4,10]:
        G=GenBA(n,i)
        nx.write_pajek(G,path+"BA/GenNetwork, n="+str(n)+" k="+str(i).replace(".",",")+".net")
    print "BA done for n="+str(n)
    
    for i in [2,4,6]:
        G=GenCM(n,"Poisson",i)
        nx.write_pajek(G,path+"CM/GenNetPoisson, n="+str(n)+" landa="+str(i).replace(".",",")+".net")
    print "CM Poisson done for n="+str(n)
    
    for i in [2.2,2.5,2.7,3.0]:
        G=GenCM(n,"PowerLaw",i)
        nx.write_pajek(G,path+"CM/GenNetwork, n="+str(n)+" PL gamma="+str(i).replace(".",",")+".net")
    print "CM powerlaw done for n="+str(n)

#experiments vs real n=1000
n=1000

i=0.05
G=GenER(n,i)
v=np.random.binomial(1000,i,100000)
plt2=histogram(G, log=False, norm=True, cumu=0, n=16)
plt2.hist(v,16,cumulative=0, alpha=0.5, normed=True, range=[min(G.degree().values()),max(G.degree().values())])
plt2.show()
print "ER done for n="+str(n)
    
i=0.2
G=GenWS(n,4,i)
plt3=histogram(G, log=False, norm=True, cumu=0, n=15)
plt3.show()
print "WS done for n="+str(n)


i=4
G=GenCM(n,"Poisson",i)
v=GetDegreeDist(1000000, "Poisson", i)
plt4=histogram(G, log=False, norm=True, cumu=0, n=12)
plt4.hist(v,12,cumulative=0, alpha=0.5, normed=True, range=[1,max(G.degree().values())])
plt4.show()
print "CM Poisson done for n="+str(n)
    
i=2.5
G=GenCM(n,"PowerLaw",i)
v=GetDegreeDist(1000000, "PowerLaw", i)
plt5=histogram(G, log=True, norm=True, cumu=0, n=10)
logbins = np.logspace(np.log10(min(v)), np.log10(max(v)), 10)
plt5.hist(v, alpha=0.5, bins = logbins, cumulative=0, normed=True, range=[min(G.degree().values()),max(G.degree().values())])
#plt5.hist(v,10,cumulative=0, alpha=0.5, normed=True, range=[1,max(G.degree().values())])
plt5.show()
gamma=powerlaw(G)
print gamma
print "CM powerlaw done for n="+str(n)


'''
n=1000
i=3
G=GenBA(n,i)
gamma=powerlaw(G)
v=GetDegreeDist(1000000, "PowerLaw", i)
plt5=histogram(G, log=True, norm=True, cumu=0, n=10)
logbins = np.logspace(np.log10(min(v)), np.log10(max(v)), 10)
plt5.hist(v, alpha=0.5, bins = logbins, cumulative=0, normed=True, range=[min(G.degree().values()),max(G.degree().values())])
plt5.show()
print "BA done for n="+str(n)
print gamma
'''
path="networks/"

for n in [50, 100, 500, 1000]:
    for i in [1,2,4,10]:
        G=GenBA(n,i)
        nx.write_pajek(G,path+"BA/GenNetwork, n="+str(n)+" k="+str(i).replace(".",",")+".net")
    print "BA done for n="+str(n)
'''  