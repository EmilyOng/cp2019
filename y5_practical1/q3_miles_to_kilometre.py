#3 (Converting miles into kilometers)
#Write a program q3_miles_to_kilometre.py
#that reads a number in miles, converts it to
#kilometres, and displays the result. One mile
#is 1.60934 kilometres. Display your answer correct
#to 3 decimal places.

def miles_to_kilometre(m):
    return m*1.60934
miles=float(input("Miles: "))
print("{0} {1:.3g} {2}".format("Kilometres: ",miles_to_kilometre(miles),"km"))
