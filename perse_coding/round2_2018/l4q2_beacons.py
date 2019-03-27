from math import sqrt as s
d=int(input())
n=int(input())
x=[]
y=[]
for i in range(n):
    xx,yy=input().split()
    x.append(int(xx))
    y.append(int(yy))
counter=0
mx=[0]
my=[0]
start=0
done=False
while not done:
    k=len(mx)
    prev=counter
    for i in range(start,k):
        for j in range(n):
            if x[j]!=31000 and y[j]!=31000:
                coor=pow(mx[i]-x[j],2)+pow(my[i]-y[j],2)
                coor=s(coor)
                if coor<=d:
                    mx.append(x[j])
                    my.append(y[j])
                    x[j]=31000
                    y[j]=31000
                    counter+=1
    start=k
    if prev==counter:
        done=True
        break
    else:
        print(counter)
