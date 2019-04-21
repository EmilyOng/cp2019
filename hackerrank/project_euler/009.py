n=int(input())
for i in range(n):
    a=int(input())
    #a+b+c=n,c=n-a-b,b=n-a-c
    #(a+(b+c))=n2
    #a2+2a(b+c)+b2+c2+2bc=n2
    #a2+b2=c2
    #a2+b2=(n-(a+b))2
    #a2+b2=n2-2n(a+b)+a2+2ab+b2
    #n2-2n(a+b)+2ab=0
    #b(2n-2a)+n2-2na=0
    #b=(2na-n2)/(2n-2a)
    temp=2*a
    tp=a**2
    run=-1
    for j in range(1,a//3+1):
        aa=j
        b=abs((temp*aa-tp)//(temp-2*aa))
        mul=1
        if aa+b<a:
            #print(aa,b)
            if tp-temp*(aa+b)+2*aa*b==0:
                mul*=aa*b*(a-aa-b)
                #print(aa,b,a-aa-b)
                run=max(run,mul)
    print(run)
        
    
