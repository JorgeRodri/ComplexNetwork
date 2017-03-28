'''
Created on 22 mar. 2017

@author: jorge
'''

from generators import GenER, GenWS, GenBA
import networkx as nx
import matplotlib.pyplot as plt

'''
if __name__ == '__main__':
    pass
'''

G=GenER(100,0.1)

nx.draw(G)
plt.show()


G=GenWS(100,4,0.1)

nx.draw(G)
plt.show()


G=GenBA(100,2)

nx.draw(G)
plt.show()
