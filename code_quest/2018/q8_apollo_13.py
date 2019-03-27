test=open('test_outputs.txt','w')
with open('JudgingInputs/Prob08.in.txt','r') as f:
    lines=f.readlines()
    a=int(lines[0])
    for j in range(a):
        x,y,z=lines[j+1].split()
        pos=[x,y,z]
        for i in range(len(pos)):
            pos[i]=float(pos[i])
            if pos[i]>180:
                pos[i]-=180
            elif pos[i]<180:
                pos[i]+=180
            k="{:.2f}".format(pos[i])
            for r in range(len(str(k))):
                if k[r]=='.':
                    if r==2:
                        k="0"+k
                    elif r==1:
                        k="00"+k
                    break
            if i==len(pos)-1:
                test.write(k)
            else:
                test.write(k+" ")
        test.write("\n")
test.close()
