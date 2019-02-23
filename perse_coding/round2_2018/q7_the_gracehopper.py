s=str(input())
curr=0
count=0
for i in range(len(s)):
    if s[i]=='+':
        curr+=15
    elif s[i]=='-':
        curr+=3
    if s[i]=='#':
        curr-=4
        count+=1
        if curr<0:
            print('#'*(count))
            exit(0)
print('\\')
