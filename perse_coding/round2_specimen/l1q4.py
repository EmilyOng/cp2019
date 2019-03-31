def rev(str):
    if len(str)==0:
        return str
    return str[len(str)-1:len(str)]+rev(str[:len(str)-1])
s=str(input())
a=int(input())
w=s*a
w=rev(w)
print(w)
