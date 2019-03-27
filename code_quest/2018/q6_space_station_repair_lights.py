test=open('test_outputs.txt','w')
with open('JudgingInputs/Prob06.in.txt','r') as f:
    lines=f.readlines()
    a=int(lines[0])
    val=0
    sys=[8,4,2,1]
    led=["off","red","green","blue"]
    for i in range(a):
        b=str(lines[i+1])
        val=0
        x,y,z,w=b.split(" ")
        nums=[x,y,z,w]
        for j in range(4):
            if nums[j]=="BROKEN" or nums[j]=="BROKEN\n":
                val+=sys[j]
        if val==0:
            test.write("off off\n")
        elif val<=3:
            test.write("off "+led[val]+"\n")
        else:
            test.write(led[int(val/4)]+" "+led[int(val%4)]+"\n")
test.close()
