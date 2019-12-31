# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:11:55 2019

@author: yekta
"""

import numpy as np
import matplotlib.pyplot as plt

'''There are 4039 vertices'''
noVertice=4039
'''Number of degree of each vertex'''
noDegree=[0]*noVertice

edges=[]
for i in range(0,noVertice):
    edges.append([])
    
L = open("/home/yekta/Desktop/SmallProject/fbNetwork/facebook_combined.txt", "r").read().splitlines();
for line in range(0,len(L)):
    dummyEdge=[]
    dummy=L[line].split(' ')
    v1=(int(dummy[0]))
    v2=(int(dummy[1]))
    edges[v1].append(v2)
    edges[v2].append(v1)
    L[line]=[v1,v2]
    
for i in range(0,noVertice):
    noDegree[i]=len(edges[i])
    
degreeDist=[0]*(max(noDegree)+1)
for i in noDegree:
    degreeDist[i]=degreeDist[i]+1
              
indexVertice = np.arange(noVertice) 
indexDegree = np.arange(max(noDegree)+1)



plt.bar(indexVertice, noDegree)
plt.xlabel('Person', fontsize=15)
plt.ylabel('Number of degree', fontsize=15)
plt.title('Degree number per person', fontsize=15)
plt.savefig("/home/yekta/Desktop/SmallProject/fbNetwork/friendDist.png", dpi=200)
plt.show()



plt.bar(indexDegree, degreeDist)
plt.xlabel('Number of degree', fontsize=15)
plt.ylabel('Number of people', fontsize=15)
plt.title('Number of degree distribution', fontsize=15)
plt.savefig("/home/yekta/Desktop/SmallProject/fbNetwork/degreeDist.png", dpi=200)
plt.show()

meanValue=sum(noDegree)/noVertice

summ=0
for i in range(0,noVertice):
    summ=summ+((noDegree[i]-meanValue)**2)
variance=summ/noVertice
standartDeviance=variance**(1/2)


