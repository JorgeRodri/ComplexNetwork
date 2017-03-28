# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 16:07:05 2017

Generates the values for the tables asked for this exercise
@author: jorge
"""


path='A1-networks/'


from utils import get_stats, print_stats
from utils import convert_to_table
from os import walk

#compulsory data sets
files=['toy/circle9.net', 'toy/star.net', 'toy/graph3+1+3.net', 'toy/grid-p-6x6.net', 'model/homorand_N1000_K4_0.net', 'model/ER1000k8.net', 'model/SF_1000_g2.7.net', 'model/ws1000.net', 'real/zachary_unwh.net', 'real/airports_UW.net']
files_names=[]

#get all the files in the directory(path)
for i in ['toy/', 'model/', 'real/']:
    lstDir=walk(path+i)
    for (root, dirs, fil) in lstDir:
        for f in fil:
            files_names+=[i+f]
print(files_names)

#results=print_stats(files_names,path)
results=get_stats(files_names,path)

f=open('results.txt', 'w')
for i in results:
    for j in i:
        f.write(str(j)+',')
    f.write('\n')
f.close()

convert_to_table('results.txt', 'table.txt')
