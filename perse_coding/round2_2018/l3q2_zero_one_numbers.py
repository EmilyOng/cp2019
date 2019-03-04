def d2b(n):
    num=[]
    n=int(n)
    while n!=0:
        num.append(n%2)
        n/=2
        n=int(n)
    num.reverse()
    binary=""
    for i in num:
        binary=binary+str(i)
    return int(binary)
n=int(input())
d=n
count=0
for i in str(n):
    if i=='0' or i=='1':
        count=count
    else:
        count+=1
if count==0:
    print(n)
    exit(0)
n=1
while d2b(int(n))%d!=0:
    n+=1
print(d2b(int(n)))
