# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:38:04 2019

@author: yekta
"""
'''//////////The algorithm to find the betweenness of edges//////////'''

import copy
import numpy as np
import matplotlib.pyplot as plt



def BFS(edges,L,start):
    
    reverseEdge=[x[:] for x in [[]] * len(edges)]    
    
    distances=[0]*len(edges)
    numberWay=[0]*len(edges)
    
    into=[0]*len(edges)
    
    weights=[0]*len(L)
    ins=[0]*len(L)
    
    color=[0]*len(edges)
    color[start]=1
    
    queue=[]
    
    v1=start
    
    '''For the vertices adjoint to the start vertex'''
    
    for v2 in edges[v1]:        
        queue.append(v2)
        color[v2]=1
        numberWay[v2]=1
        distances[v2]=1
        reverseEdge[v2].append(v1)
        into[v1]=into[v1]+1
        
        indx=edges[v2].index(v1)    
        del edges[v2][indx]
        
    if not queue:
        return weights
            
    
    '''DFS search top to bottom to find number of minimum paths'''
    while(queue):
        
        v1=queue.pop(0)
        
        for v2 in edges[v1]:
            
            if color[v2]==0:
                queue.append(v2)
                color[v2]=1
                distances[v2]=distances[v1]+1
            
            if (distances[v1] >= distances[v2]):
                continue
            else:
                numberWay[v2]=numberWay[v1]+numberWay[v2]
                reverseEdge[v2].append(v1)
                into[v1]=into[v1]+1
                
            indx=edges[v2].index(v1)
            del edges[v2][indx]
            
            
    '''Number of shortest path from start vertex to other vertices has found so far, saved in distances array'''
    numberWay[start]=1
    
           
    #print(numberWay)
    try:
        v1=into.index(0)
        into[v1]=-1
    except:
        v1=-2
    while(v1!=-2):
        
        denum=0        
        for v2 in reverseEdge[v1]:
            denum=denum+numberWay[v2]
        
        weight=ins[v1]+1
        
        for v2 in reverseEdge[v1]:
            
            if v2>v1:
                idx=L.index([v1,v2])
            else:
                idx=L.index([v2,v1])
            
            weights[idx]= (weight * numberWay[v2]) / denum
            
            into[v2]=into[v2]-1
            ins[v2]=weights[idx]+ins[v2]
        
        try:
            v1=into.index(0)
            into[v1]=-1
        except:
            v1=-2
    
    #print(weights)        
    return weights       
    
    
def main():
    noVertice=4039
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
        if v2 > v1:
            L[line]=[v1,v2]
        else:
            L[line]=[v2,v1]
        
    betweenness=[0]*len(L)
    
    
    for vert in range(0,noVertice):
        edgesDummy=copy.deepcopy(edges)
        weightDummy=BFS(edgesDummy,L,vert)
        betweenness=[a + b for a, b in zip(betweenness, weightDummy)]
        print(vert)
        
    print("Writing \n")
    
    with open("/home/yekta/Desktop/SmallProject/fbNetwork/output.txt", "w") as f:
        for s in betweenness:
            f.write(str(s) +"\n")
            
    print("Mission completed \n")

if __name__ == '__main__':
    main()
        
     

'''//////////The part where results are examined//////////'''
betweenness = open("/home/yekta/Desktop/SmallProject/fbNetwork/output.txt", "r").read().splitlines();
betweenness=[float(x) for x in betweenness]    

noVertice=4039
importance=[0]*noVertice
degree=[0]*noVertice

    
L = open("/home/yekta/Desktop/SmallProject/fbNetwork/facebook_combined.txt", "r").read().splitlines();
for line in range(0,len(L)):
    dummy=L[line].split(' ')
    v1=(int(dummy[0]))
    v2=(int(dummy[1]))
    L[line]=[v1,v2]
    importance[v1]=importance[v1]+betweenness[line]
    importance[v2]=importance[v2]+betweenness[line]
    degree[v1]=degree[v1]+1
    degree[v2]=degree[v2]+1
    
avgImportance=copy.deepcopy(importance)

for i in range(0,noVertice):
    avgImportance[i]= (avgImportance[i])/(degree[i])   

indexVertice = np.arange(noVertice) 


plt.bar(indexVertice, importance)
plt.xlabel('Person', fontsize=15)
plt.ylabel('Total betweenness', fontsize=15)
plt.title('Total betweenness per person', fontsize=15)
plt.savefig("/home/yekta/Desktop/SmallProject/fbNetwork/importance.png", dpi=200)
plt.show()

plt.bar(indexVertice, avgImportance)
plt.xlabel('Person', fontsize=15)
plt.ylabel('Averaged betweenness', fontsize=15)
plt.title('Averaged betweenness per person', fontsize=15)
plt.savefig("/home/yekta/Desktop/SmallProject/fbNetwork/avgImportance.png", dpi=200)
plt.show()
