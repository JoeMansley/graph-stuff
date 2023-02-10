#Given the adjacency list of a directed graph, output an Euler path. If none exists, output false.
#Assume vertices have labels 0,1,...n-1
#Example input would be [{1},{},{0}], which should give output [2,0,1]

from copy import deepcopy

def EulerPath(inputAdjList):
    adjList=deepcopy(inputAdjList)
    
    inDeg=[0]*len(adjList)
    for a in adjList:
        for k in a:
            inDeg[k]+=1
            
    v1=0
    for j,a in enumerate(adjList):
        d=len(a)-inDeg[j] #outdegree - indegree
        if d==1:
            v1=j
            break
        elif d>1 or d<-1:
            return False

    def walkFrom(u):
        walk=[u]
        while adjList[walk[-1]]:
            walk.append(adjList[walk[-1]].pop())
        return walk
    
    path=walkFrom(v1)
    k=0
    while k<len(path):
        if adjList[path[k]]:
            path=path[:k]+walkFrom(path[k])+path[k+1:]
        else:
            k+=1
            
    if any(adjList):
        return False
    return path
