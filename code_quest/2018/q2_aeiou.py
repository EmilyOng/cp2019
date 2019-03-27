with open('ExampleInputs/Prob02.in.txt','r') as f:
    lines = f.readlines()
    a=int(lines[0])
    for i in range(a):
        track=0
        for j in lines[i+1]:
            if j=='a' or j=='i' or j=='o' or j=='u' or j=='e':
                track+=1
        print(track)
