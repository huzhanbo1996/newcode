#pass
from typing import *
# We can easily reuse the algo in #1001 whith dijstra shortests algo to get
# all the shortest paths.
# Instead of it, there is a simplier methods using only DFS to brute force 
# all the paths avaible. And we choose the shortest.

def dfs(graphe:List[List[int]],departure:int,arrival:int,path:List[int],shortCost2Points:List[int]) -> List[List[int]]:
    if departure==arrival:
        return [path+[arrival]]
    nextPoints = [i for i,p in enumerate(graphe[departure]) if p!=float("inf") and not i in path]
    nextPointsAfter = []
    for p in nextPoints:
        if shortCost2Points[p]>=shortCost2Points[departure]+graphe[departure][p]:
            shortCost2Points[p]=shortCost2Points[departure]+graphe[departure][p]
            nextPointsAfter.append(p)
    ans=[]
    for p in nextPointsAfter:
        ans.extend(dfs(graphe,p,arrival,path+[departure],shortCost2Points))
    return ans

def DFS(graphe:List[List[int]],departure:int,arrival:int) -> List[List[int]]:
    return dfs(graphe,departure,arrival,[],[float("inf") if i!=departure else 0 for i in range(len(graphe))])

def valueOfPath(graphe:List[List[int]],path:List[int]) ->int:
    v=0
    for i,p in enumerate(path):
        if i==len(path)-1:
            break
        v+=graphe[p][path[i+1]]
    return v


def maxValueAndAveValue(value:List[int],path:List[int],nameList:Dict[int,str]) -> Tuple[int,int]:
    sumV=0
    for p in path:
        sumV+=value[p]
    return sumV,int(sumV/(len(path)-1))    

def path2Str(path:List[int],list2Name:Dict[int,str]) ->str:
    names=[list2Name[p] for p in path]
    return "->".join(names)

def algo():
    inputTmp=input().split()
    numPoints,numVex,departure = int(inputTmp[0]),int(inputTmp[1]),inputTmp[2]
    value=[0]
    nameList={departure:0}
    list2Nmae={0:departure}
    graphe=[[float("inf") for i in range(numPoints)] for j in range(numPoints)]
    for i in range(numPoints-1):
        inputTmp=input().split()
        name,v= inputTmp[0],int(inputTmp[1])
        value.append(v)
        nameList[name]=i+1
        list2Nmae[i+1]=name
    for i in range(numVex):
        inputTmp=input().split()
        fromP,toP,v= inputTmp[0],inputTmp[1],int(inputTmp[2])
        graphe[nameList[fromP]][nameList[toP]]=v
        graphe[nameList[toP]][nameList[fromP]]=v

    paths=DFS(graphe,nameList[departure],nameList["ROM"])

    pathsTmp=[]
    minCost=float("inf")
    for p in paths:
        if valueOfPath(graphe,p)<minCost:
            minCost=valueOfPath(graphe,p)
            pathsTmp=[p]
        elif valueOfPath(graphe,p)==minCost:
            pathsTmp.append(p)
    paths=pathsTmp

    ans=[]
    maxAll=float("-inf")
    for p in paths:
        maxV,aveV = maxValueAndAveValue(value,p,list2Nmae)
        if maxV>maxAll:
            maxAll=maxV
            ans=[(maxV,aveV,p)]
        elif maxV==maxAll:
            ans.append((maxV,aveV,p))
    
    maxAve=max(ans,key=lambda x:x[1])

    print(str(len(paths))+" "+str(valueOfPath(graphe,maxAve[2]))+" "+str(maxAve[0])+" "+str(maxAve[1]))
    print(path2Str(maxAve[2],list2Nmae))
    return

    

if __name__ == "__main__":
    algo()


"""
6 7 HZH
ROM 100
PKN 40
GDN 55
PRS 95
BLN 80
ROM GDN 1
BLN ROM 1
HZH PKN 1
PRS ROM 2
BLN HZH 2
PKN GDN 1
HZH PRS 1
"""