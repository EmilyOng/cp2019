stepping_stones=int(input())
num_players=int(input())
counting_num=int(input())
rounds=int(input())
org=rounds
stones=[]
for i in range(num_players):
    stones.append('r')
space=(stepping_stones-(num_players*2))//2
for i in range(num_players,num_players+space+1):
    stones.append('_')
for i in range(num_players+space+1,stepping_stones):
    stones.append('b')
m=num_players-1
while rounds>0:
    left_player=stones[m]
    right_player=stones[-m]
    for i in range(m+1,stepping_stones):
        if stones[i]=='_':
            if i-m<=2:
                stones[i]='r'
                stones[m]='_'
                break
    for i in range(stepping_stones-m-1,0,-1):
        if stones[i]=='_':
            if stepping_stones-m-1-i<=2:
                stones[i]='b'
                stones[stepping_stones-m-1]='_'
                break
    m+=counting_num+1
    if m>num_players:
        m-=num_players
    m-=1
    rounds-=1
    if rounds==org-1:
        for stone in stones:
            print(stone,end="")
        print()

for stone in stones:
    print(stone,end="")
