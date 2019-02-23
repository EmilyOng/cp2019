#6 (Conversion from kilograms to pounds) q06_kilograms_to_pounds.py
#Write a program that displays the following table
#(1 kilogram = 2.2 pounds):

#Kilograms Pounds
#1         2.2
#2         4.4
#3         6.6
#...
#9         19.8
#10        22.0

def kilo_to_pounds(limit):
    print("Kilogram","\t","Pounds")
    for i in range(limit):
        print("{0}{2} {1:.1f}".format(i+1,(i+1)*2.2,"\t\t"))
        
kilo_to_pounds(20)

