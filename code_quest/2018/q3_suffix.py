test=open('test_outputs.txt','w')
with open('JudgingInputs/Prob03.in.txt','r') as f:
    lines=f.readlines()
    a=int(lines[0])
    for i in range(a):
        s=str(lines[i+1])
        for j in range(len(s)):
            if s[j].isalpha():
                if j>=2 and ((s[j-1]==s[j-2] and int(s[j-1])==1) or
                             (s[j-2:j]=='11' or s[j-2:j]=='12' or s[j-2:j]=='13')):
                    test.write(s[:j]+"th"+"\n")
                #st nd rd th
                elif s[j-1]=='1':
                    test.write(s[:j]+"st"+"\n")
                elif s[j-1]=='2':
                    test.write(s[:j]+"nd"+"\n")
                elif s[j-1]=='3':
                    test.write(s[:j]+"rd"+"\n")
                else:
                    test.write(s[:j]+"th"+"\n")
                break

test.close()
