a=int(input())
track=1
def rev(str):
    if len(str)==0:
        return str
    return str[len(str)-1:len(str)]+rev(str[:len(str)-1])
total=a+int(rev(str(a)))
while str(total)!=rev(str(total)):
    total+=int(rev(str(total)))
    track+=1
print(track)
