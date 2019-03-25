a=int(input())
coins=a
while a!=-1:
    a=int(input())
    if a!=-1:
        coins+=a
print(int(coins/60)*30)
