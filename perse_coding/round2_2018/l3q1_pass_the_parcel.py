p,t,w=input().split()
p=int(p)
t=int(t)
w=int(w)
alpha=list(map(chr,range(ord('A'),ord('Z'))))
players=[]
for i in range(p):
    players.append(alpha[i])
step=0
layers=w
while layers!=0:
    step+=t
    if layers!=w:
        step-=1
    if step>=len(players):
        residue=step-len(players)
        step=residue%len(players)
    if len(players)==1:
        print(players[0])
        exit(0)
    elif layers==1:
        print(players[step])
        exit(0)
    players.remove(players[step])
    layers-=1
