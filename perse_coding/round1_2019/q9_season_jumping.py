s=["spring","summer","autumn","winter"]
w=str(input())
a=int(input())

if w=="summer":
    counter=1+a
    print(s[counter%4])
elif w=="spring":
    counter=0+a
    print(s[counter%4])
elif w=="autumn":
    counter=2+a
    print(s[counter%4])
else:
    counter=3+a
    print(s[counter%4])
