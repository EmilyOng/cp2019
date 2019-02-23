#11 (Computing the greatest common divisor)  q11_find_gcd.py
#A solution to find the greatest common divisor of two
#integers n1 and n2 is as follows: First find d to be the
#minimum of n1 and n2, then check whether d, d-1, ... d-2, 2,
#or 1 is a divisor for both n1 and n2 in this order. The first
#such common divisor is the greatest common divisor for n1 and n2.
#Write a program to implement this solution.

def find_gcd(n1,n2):
    d=min(n1,n2)
    for i in range(d,0,-1):
        if n1%i==0 and n2%i==0:
            print("The gcd of",n1,"&",n2,"is",i,end=".")
            exit(0)

def euclid(n1,n2):
    if n2==0:
        return n1
    else:
        return euclid(n2,n1%n2)
n1=int(input())
n2=int(input())
print("The gcd of",n1,"&",n2,"is",euclid(n1,n2),end=".")
find_gcd(n1,n2)
