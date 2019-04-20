n=int(input())
for i in range(n):
    a=int(input())
    if a%12==0:
        scale=a//12
        print(12*scale)
    else:
        print(-1)
