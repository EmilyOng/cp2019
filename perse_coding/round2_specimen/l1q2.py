s=str(input())
a=int(input())
if len(s)==a:
    print("MATCH")
elif len(s)>a:
    print("MORE")
else:
    print("FEWER")
