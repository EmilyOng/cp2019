test=open('test_outputs.txt','w')
def rev(w):
    if len(w)==0:
        return w
    return w[len(w)-1:len(w)]+rev(w[:len(w)-1])
with open('JudgingInputs/Prob07.in.txt','r') as f:
    lines=f.readlines()
    a=int(lines[0])
    i=0
    while a!=0:
        x=int(lines[i+1])
        a-=1
        none=[]
        track=1
        for j in range(i+2,x+i+2):
            s=str(lines[j]).lower().rstrip()
            ss=str(rev(s)).rstrip()
            if s!=ss:
                none.append(track)
            track+=1
        i=(x+i+1)
        if len(none)==0:
            test.write("True\n")
        else:
            test.write("False - ")
            for k in range(len(none)):
                if k==len(none)-1:
                    test.write(str(none[k]))
                else:
                    test.write(str(none[k])+", ")
            test.write("\n")
test.close()
