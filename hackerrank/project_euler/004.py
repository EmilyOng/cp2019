def rev(n):
    if len(n)==0:
        return n
    else:
        return n[len(n)-1:len(n)]+rev(n[:len(n)-1])
a=int(input())
from math import sqrt as s
for i in range(a):
    x=int(input())
    x-=1
    out=False
    while not out:
        x=str(x)
        y=rev(x)
        out=False
        if x==y:
            y=int(y)
            for j in range(int(s(y)),1,-1):
                if y%j==0 and len(str(j))==3 and len(str(y//j))==3:
                    print(y)
                    out=True
                    break
            x=int(x)
            x-=1
        else:
            x=int(x)
            x-=1
