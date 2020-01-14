#pass
from typing import *

#all availble paths
def disjstra(nums:List[List[int]],departure:int,arrival:int,paths:List[List[int]],minPaths:List[int],pointsInclu:List[int]):
    
    _minPaths=minPaths[:]
    toPointNow=minPaths[departure]
    nextP=nums[departure]
    for i,p in enumerate(nextP):
        if p+toPointNow==float("inf"):
            continue
        if p+toPointNow<_minPaths[i]:
            _minPaths[i]=p+toPointNow
            paths[i]=[departure]
        elif p+toPointNow==_minPaths[i]:
            paths[i].append(departure)
    
    if departure==arrival:
        return [paths]

    _pointsInclu=pointsInclu[:]+[departure]
    nextPoints=[]
    minNext=float("inf")
    for p in range(len(nums)):
        if p in _pointsInclu:
            continue
        if _minPaths[p]<minNext:
            minNext=_minPaths[p]
            nextPoints=[p]
        elif _minPaths[p]==minNext:
            nextPoints.append(p)

    ans=[]
    disjstra(nums,nextPoints[0],arrival,paths,_minPaths,_pointsInclu)
    return 

def helperBuildPaths(departure:int,arrival:int,paths:List[List[int]],before:List[List[int]]) -> List[List[int]]:
    if departure==arrival:
        return before
    ans=[]
    for p in paths[arrival]:
        now=[]
        for b in before:
            now.append(b[:]+[p])
        ans.extend(helperBuildPaths(departure,p,paths,now))
    return ans
    
def rebuildPaths(departure:int,arrival:int,paths:List[List[int]]) -> List[List[int]]:
    ans=helperBuildPaths(departure,arrival,paths,[[arrival]])
    return [i[::-1] for i in ans]

def numSentByCneter(value:List[int],Cmax:int,departure:int,arrival:int,path:List[int]) -> (int,int):
    target=int(Cmax/2)
    rest=0
    need=0
    for p in path[1:]:
        diff=value[p]-target
        if diff<0:
            if rest<abs(diff):
                need+=abs(diff)-rest
                rest=0
            else:
                rest-=abs(diff)
        else:
            rest+=diff

    return need,rest

def path2Str(path:List[int])->str:
    return "->".join([str(p) for p in path])

def algo():
    inputTmp=input().split()
    Cmax,N,Sp,M = [int(i) for i in inputTmp]

    inputTmp=input().split()
    value=[0]+[int(i) for i in inputTmp]

    raodMap=[[float("inf") for i in range(N+1)] for j in range(N+1)]

    for i in range(M):
        inputTmp=input().split()
        depart,attest,poids=[int(j) for j in inputTmp]
        raodMap[depart][attest]=poids
        raodMap[attest][depart]=poids

    tmp=[float("inf") for i in range(len(raodMap))]
    tmp[0]=0
    paths=[[] for i in range(len(raodMap))]
    disjstra(raodMap,0,Sp,paths,tmp,[])
    paths=rebuildPaths(0,Sp,paths)

    ans=[]
    sents=[]
    for p in paths:
        sent,rest = numSentByCneter(value,Cmax,0,Sp,p)
        ans.append((sent,rest,p))
        sents.append(sent)
    
    sent=min(sents)
    rests=[a[1] for a in ans if a[0]==sent]
    rest=min(rests)
    for a in ans:
        if a[0]==sent and a[1]==rest:
            print(str(sent)+" "+path2Str(a[2])+" "+str(rest))
    return

if __name__ == "__main__":
    algo()
    pass

"""
10 3 3 5
6 7 0
0 1 1
0 2 1
0 3 3
1 3 1
2 3 1
"""

"""
10 4 4 7
6 7 0 2
0 1 1
1 3 2
1 2 1
2 3 1
0 3 3
3 4 1
0 4 4
"""