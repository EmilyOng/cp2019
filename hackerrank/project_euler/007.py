from math import sqrt as s
primes=[]
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
primes.append(2)
for i in range(n):
    a=int(input())
    if len(primes)>=a:
        print(primes[a-1])
    else:
        start=primes[len(primes)-1]+1
        count=len(primes)
        while True:
            if prime(start):
                primes.append(start)
                count+=1
            if count==a:
                print(start)
                break
            start+=1
