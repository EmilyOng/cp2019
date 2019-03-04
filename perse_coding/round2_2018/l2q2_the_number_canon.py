n=int(input())
step=1
count=1
canon=0
for i in range(n):
    for j in range(step):
        canon+=count
        count+=1
    step+=1
print(canon)
        
    
