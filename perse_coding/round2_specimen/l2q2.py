s=input()
ss=s.split(" ")
for i in range(len(ss)):
    ss[i]=ord(ss[i])
ss.sort()
print(int(ss[len(ss)-1])-int(ss[0]))
