n=int(input())
from math import sqrt as s
for i in range(n):
    a=int(input())
    num=[]
    for f in range(a+1):
        num.append(0)
    #reduce
    for j in range(1,a+1):
        #print(j,":",end=" ")
        for k in range(2,int(s(j))+1):
            counter=0
            if j%k==0:
                while j%k==0:
                    j//=k
                    counter+=1
                while num[k-1]<counter:
                    if num[k-1]==counter:
                        break
                    num[k-1]+=1
                #print(k,"^",counter,end=" ")
        if j!=1:
            while num[j-1]<1:
                if num[j-1]==1:
                       break
                num[j-1]+=1
            #print(j,"^",1,end=" ")
    total=1
    for np in range(a+1):
        if num[np]!=0:
            total*=pow((np+1),num[np])
    print(total)
