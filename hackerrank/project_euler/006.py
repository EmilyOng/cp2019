from math import sqrt as s
n=int(input())
for k in range(n):
    a=int(input())
    total=(a*(a+1))>>1
    total=pow(total,2)
    print(total-(a*(2*a+1)*(a+1))//6)
