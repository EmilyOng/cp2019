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

for i in range(n):
    for j in range(row):
        if capacity[j]>=sizes[i]:
            capacity[j]-=sizes[i]
            tickets+=sizes[i]
            break

print(tickets)
