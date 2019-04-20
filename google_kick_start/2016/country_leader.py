infile=open("A-large-practice.in","r")
a=int(infile.readline().strip())
outfile=open("country_leader.out","w")
for i in range(a):
    n=int(infile.readline().strip())
    curr_max=-1
    curr_leader=0
    leaders=[]
    for j in range(n):
        size=[]
        s=str(infile.readline().strip())
        leaders.append(s)
        for k in s:
            if k!=' ':
                size.append(k)
        size=set(size)
        if len(size)>curr_max:
            curr_max=len(size)
            curr_leader=j
        if len(size)==curr_max and leaders[j]<leaders[curr_leader]:
            curr_leader=j
    outfile.write("Case #"+str(i+1)+": ")
    outfile.write(leaders[curr_leader])
    outfile.write("\n")
outfile.close()
infile.close()
