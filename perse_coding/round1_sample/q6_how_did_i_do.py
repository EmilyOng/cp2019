a=['st','nd','rd','th','th']
for i in range(0,5):
    name=str(input())
    if name=="Ellie":
        print("{0}{1}".format(i+1,a[i]))
