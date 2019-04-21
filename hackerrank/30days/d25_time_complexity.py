# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt as s
def prime(p):
    if p==2:
        return True
    if p<2:
        return False
    for pp in range(2,int(s(p))+1):
        if p%pp==0:
            return False
    return True
n=int(input())
pprime=[2]
for i in range(n):
    a=int(input())
    pprime.sort()
    if a in pprime:
        print("Prime")
    else:
        if prime(a):
            pprime.append(a)
            print("Prime")
        else:
            print("Not prime")
