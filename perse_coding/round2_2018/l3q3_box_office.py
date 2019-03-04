row,seat=input().split()
row=int(row)
seat=int(seat)
n=int(input())
capacity=[]
for i in range(row):
    capacity.append(seat)
tickets=0
curr_row=0
sizes=[]
for i in range(n):
    size=int(input())
    sizes.append(size)

sizes.sort()
for i in range(n):
    size=sizes[i]
    if size>capacity[curr_row]:
        if curr_row+1>=row:
            tickets=tickets
        else:
            curr_row+=1
            capacity[curr_row]-=size
            tickets+=size
    else:
        capacity[curr_row]-=size
        tickets+=size
        
print(tickets)
