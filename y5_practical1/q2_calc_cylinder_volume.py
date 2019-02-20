#2 (Computing the volume of a cylinder)
#C reads in the radius and length of a cylinder
#and computes its volume using the following formulae:
#area = radius * radius * pi
#volume = area * length
import math
def find_area(radius):
    return radius*radius*math.pi

C_radius=int(input("Radius: "))
C_length=int(input("Length: "))
print("{0} {1:.3g}".format("Volume: ",find_area(C_radius)*C_length))
