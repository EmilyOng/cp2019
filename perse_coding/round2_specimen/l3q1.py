def rev(str):
    if len(str)==0:
        return str
    return str[len(str)-1:len(str)]+rev(str[:len(str)-1])
s=str(input())
palindrome=False
ptr=1
while not palindrome:
    ps=rev(s)
    if ps==s:
        print(ps)
        exit(0)
    for i in range(len(s)):
        ss=s
        ss=ss.replace(ss[i],"",1)
        sss=rev(ss)
        if ss==sss:
            palindrome=True
            print(ss)
            exit(0)
    s=s[ptr:len(s)]
    ptr+=1
