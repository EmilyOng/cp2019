f=open('JudgingOutputs/Prob08.out.txt','r')
ff=open('test_outputs.txt','r')
a=f.readlines()
b=ff.readlines()
if a==b:
    print("CORRECT")
else:
    print("WRONG")
