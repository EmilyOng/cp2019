fib=[]
fib.append(1)
fib.append(2)
def gen_fib(end):
    i=2
    total=2
    while True:
        fib.append(0)
        fib[i]=fib[i-1]+fib[i-2]
        if fib[i]>=end:
            return total
        if fib[i]%2==0:
            total+=fib[i]
        i+=1
a=int(input())
for i in range(a):
    n=int(input())
    print(gen_fib(n))
