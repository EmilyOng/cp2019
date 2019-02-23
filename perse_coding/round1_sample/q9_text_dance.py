start=0
a=input()
if a=='<':
    start=0
elif a=='+':
    start=1
elif a=='&':
    start=2
else:
    start=3
moves=['<','+','&','>']
cycles=[moves[start]]
start+=1
for i in range(0,7):
    if start>3:
        start=0
    cycles.append(moves[start])
    start+=1
for i in cycles:
    print(i,end="")
