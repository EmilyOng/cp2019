a=int(input())
if a==1:
    print(11)
    exit(0)
elif a==2:
    print(21)
    exit(0)
elif a==3:
    print(1211)
    exit(0)
else:
    s="1211"
    for j in range(a-3):
        cmp=s[0]
        counter=1
        letter=""
        for i in range(1,len(s)):
            if s[i]==cmp:
                counter+=1
            else:
                letter=letter+str(counter)+cmp
                cmp=s[i]
                counter=1
        letter=letter+str(counter)+cmp
        s=letter
    print(letter)
