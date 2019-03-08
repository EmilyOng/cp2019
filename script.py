import os
path="/Users/emilyong/cp2019"
dirs=os.listdir(path)
file=open("README.md","w+")
counter=0
for i in dirs:
    if not os.path.isfile(i) and i!=".git":
        file.write("<h2>"+i+"</h2>")
        for j in os.listdir(i):
            if j!=".DS_Store":
                if os.path.isfile(path+"/"+i+"/"+j):
                    file.write("<b>"+i+"</b>"+"/"+j+"</br>")
                else:
                    for k in os.listdir(path+"/"+i+"/"+j):
                        file.write("<b>"+i+"</b>"+"/"+"<b>"+j+"</b>"+"/"+k+"</br>")
        file.write("</br></br>")

file.close()
