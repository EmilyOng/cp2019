with open('ExampleInputs/Prob01.in.txt','r') as f:
    lines = f.readlines()
    a=int(lines[0])
    for i in range(a):
        if int(lines[i+1])>=70:
            print("PASS")
        else:
            print("FAIL")
