test=open('test_outputs.txt','w')
with open ('JudgingInputs/Prob04.in.txt','r') as f:
    lines=f.readlines()
    a=int(lines[0])
    moves={'R':'S','S':'P','P':'R'}
    players={'R':'ROCK','S':'SCISSORS','P':'PAPER'}
    for i in range(a):
        b=str(lines[i+1])
        curr_winner=b[0]
        r=int(b.count('R'))
        s=int(b.count('S'))
        p=int(b.count('P'))
        #rock->scissors, scissors->paper,paper->rock
        if r>0 and s>0 and p>0:
            test.write("NO WINNER"+"\n")
            continue
        elif r>0 and s>0:
            if r==1:
                test.write("ROCK"+"\n")
            else:
                test.write("NO WINNER"+"\n")
            continue
        elif s>0 and p>0:
            if s==1:
                test.write("SCISSORS"+"\n")
            else:
                test.write("NO WINNER"+"\n")
        elif p>0 and r>0:
            if p==1:
                test.write("PAPER"+"\n")
            else:
                test.write("NO WINNER"+"\n")
        else:
            test.write("NO WINNER"+"\n")
test.close()
