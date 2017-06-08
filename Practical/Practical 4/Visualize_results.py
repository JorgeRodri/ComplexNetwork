'''
Created on 27 may. 2017

@author: jorge
'''

import pickle
from numpy import linspace
import matplotlib.pyplot as plt
from os import walk



path='Network_results/'
save_path='figures/'
if __name__ == '__main__':
    file_names=[]
    lstDir=walk(path)
    for (root, dirs, fil) in lstDir:
        for f in fil:
            file_names+=[f]
            
    for network in file_names:
        with open(path+network, 'rb') as f:
            ros=pickle.load(f)
        beta=linspace(0,1,51)
        plt.plot(beta,ros,'o-')
        plt.xlabel('Betas')
        plt.ylabel('p')
        plt.title('p Changes over Beta')
        plt.savefig(save_path+network[0:-4]+'.jpg')
        plt.show()
