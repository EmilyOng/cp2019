p=int(input())
t=int(input())
w=int(input())
alpha=list(map(chr,range(ord('A'),ord('Z'))))
players=[]
for i in range(p):
    players.append(alpha[i])
step=0
while w!=0:
    
