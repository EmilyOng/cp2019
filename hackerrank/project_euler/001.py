a=int(input())
for i in range(a):
    n=int(input())
    n-=1
    if n%3==0:
        m3=n//3
    else:
        m3=(n-(n%3))//3
    if n%5==0:
        m5=n//5
    else:
        m5=(n-(n%5))//5
    if n%15==0:
        m15=n//15
    else:
        m15=(n-(n%15))//15
    m3=m3*(m3+1)>>1
    m5=m5*(m5+1)>>1
    m15=m15*(m15+1)>>1
    print(int(m3*3+m5*5-m15*15))
