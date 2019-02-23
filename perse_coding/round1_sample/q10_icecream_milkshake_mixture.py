a=str(input())
icecream=0
milk=0
cream=0
for i in a:
    if i=='I':
        icecream+=1
    elif i=='M':
        milk+=1
    else:
        cream+=1
if icecream!=2:
    print('I')
elif milk!=1:
    print('M')
else:
    print('C')
