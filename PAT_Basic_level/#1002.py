#pass
if __name__ == "__main__":
    nums=input().split()
    nums=[int(i) for i in nums[1:]]
    A1,A2,A3,A4,A5= [],[],[],[],[]
    for n in nums:
        if n%5==0:
            A1.append(n)
        elif n%5==1:
            A2.append(n)
        elif n%5==2:
            A3.append(n)
        elif n%5==3:
            A4.append(n)
        else:
            A5.append(n)
    A1=[i for i in A1 if i%2==0]
    a1="N" if len(A1)==0 else sum(A1)

    A2=[n if i%2==0 else -n for i,n in enumerate(A2)] 
    a2="N" if len(A2)==0 else sum(A2)

    a3="N" if len(A3)==0 else len(A3)

    a4=0
    if len(A4)==0:
        a4="N"
    else:
        a4=round(sum(A4)/len(A4),ndigits=1)
    
    a5="N" if len(A5)==0 else max(A5)

    print(str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4)+" "+str(a5))