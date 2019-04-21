n=int(input())
from math import sqrt as s
def prime(p):
    if p<2:
        return False
    if p==2:
        return True
    for pp in range(2,int(s(p))+1):
        if p%pp==0:
            return False
    return True
primes=[2]
corr=[2]
pdict={}
for i in range(n):
    a=int(input())
    total=0
    lprime=primes[len(primes)-1]
    if lprime==a:
        print(corr[len(corr)-1])
    elif lprime>a:
        #find closest prime <= a
        curr=a
        while True:
            if prime(curr):
                break
            else:
                curr-=1
        print(pdict[curr])
    else:
        #build corr,a>lprime
        for j in range(lprime+1,a+1):
            if prime(j):
                primes.append(j)
                corr.append(corr[len(corr)-1]+j)
                pdict[j]=corr[len(corr)-1]
        print(corr[len(corr)-1])
