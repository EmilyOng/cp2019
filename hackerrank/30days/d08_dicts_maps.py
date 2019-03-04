# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneBook=dict()
n=int(input())
for i in range(n):
    s,k=input().split()
    phoneBook[s]=k
for j in range(n):
    t=str(input())
    if t in phoneBook:
        print(t+"="+phoneBook[t])
    else:
        print("Not found")
