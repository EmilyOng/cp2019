s=str(input())
ss=s.split(" ")
k=0
deduct=False
for i in range(6):
    if int(ss[i])==13:
        if i<5:
            deduct=True
    else:
        if not deduct:
            k+=int(ss[i])
        else:
            deduct=False
print(k)
