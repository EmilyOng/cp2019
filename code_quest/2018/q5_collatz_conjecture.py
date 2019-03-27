test=open('test_outputs.txt','w')
with open('JudgingInputs/Prob05.in.txt','r') as f:
    lines=f.readlines()
    a=int(lines[0])
    for i in range(a):
        b=int(lines[i+1])
        c=b
        counter=1
        while b!=1:
            if b%2==0:
                b/=2
            else:
                b=(3*b)+1
            counter+=1
        test.write(str(c)+":"+str(counter)+"\n")
test.close()
