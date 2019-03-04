import os
path="/Users/emilyong/cp2019"
dirs=os.listdir(path)
file=open("README.md","w+")
counter=0
for i in dirs:
    if not os.path.isfile(i) and i!=".git":
        for j in os.listdir(i):
            if j!=".DS_Store":
                if os.path.isfile(path+"/"+i+"/"+j):
                    file.write(i+"/"+j+"\n")
                else:
                    for k in os.listdir(path+"/"+i+"/"+j):
                        file.write(i+"/"+j+"/"+k+"\n")
        file.write("\n")

file.close()
