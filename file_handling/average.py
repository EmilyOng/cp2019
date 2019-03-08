file=open("numbers.txt","r")
lines=file.readlines()
total=0
for i in range(len(lines)):
    total+=int(lines[i])
average=int(total/len(lines))
file.close()
file=open("numbers.txt","a")
file.write("\n"+"The average of the sum is "+str(average))
file.close()
