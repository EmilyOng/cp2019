#2 (Validating triangles and computing perimeter) q02_triangle.py
#Write a program that reads three edges for a triangle
#and determines whether the input is valid. The input is
#valid if the sum of any two edges is greater than the third edge.
#The program will compute the perimeter of the triangle if the input
#is valid. Otherwise, display that the input is invalid.

def triangle(s1,s2,s3):
    if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
        print("{0} {1}".format("Perimeter = ",s1+s2+s3))
    else:
        print("Invalid triangle!")

side1=int(input("Enter side 1: "))
side2=int(input("Enter side 2: "))
side3=int(input("Enter side 3: "))
triangle(side1,side2,side3)
