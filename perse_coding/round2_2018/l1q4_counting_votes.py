a=int(input())
yes=0
no=0
for i in range(0,a):
    s=str(input())
    if s=='YES':
        yes+=1
    elif s=='NO':
        no+=1
print("YES",yes)
print("NO",no)
