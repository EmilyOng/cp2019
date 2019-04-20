n=int(input())
for i in range(n):
    a,b=input().split(" ")
    a=int(a)
    b=int(b)
    c=str(input())
    mul=1
    run=0
    for j in range(a):
        if j+b-1<a:
            for k in range(j,j+b):
                mul*=int(c[k])
            run=max(run,mul)
            mul=1
    print(run)
