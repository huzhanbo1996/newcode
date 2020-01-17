from functools import cmp_to_key
s1=input()
N,M = [int(x) for x in s1.split()]
jobs=[]
friends=[]
for i in range(N):
    s1=input()
    i1,i2 = [int(x) for x in s1.split()]
    jobs.append((i1,i2))

s1=input()
i1 = [(int(x),-1) for x in s1.split()]
jobs.extend(i1)

jobs=sorted(jobs,key=cmp_to_key(lambda x,y:x[0]-y[0]))

for i in range(len(jobs)):
    if jobs[i][1]==-1:
        print(str((max(jobs[0:i],key=lambda x:x[1])[1])))