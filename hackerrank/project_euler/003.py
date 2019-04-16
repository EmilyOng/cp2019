from math import sqrt as s
def check(c):
    if c<2:
        return False
    if c==2:
        return True
    for i in range(2,int(s(c))+1):
        if c%i==0:
            return False
    return True
n=int(input())
for k in range(n):
    a=int(input())
    if check(a):
        print(a)
    else:
        m=2
        for i in range(2,int(s(a))+1):
            while a%i==0:
                m=max(2,i)
                a//=i
        if check(a) and a>m:
            print(a)
        else:
            print(m)          
