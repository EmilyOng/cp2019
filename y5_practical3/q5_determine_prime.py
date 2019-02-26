#5 (Prime number) q6_determine_prime.py
#Write a function to determine whether an integer
#is a prime number. An integer greater than 1 is a
#prime number if its only divisor is 1 or itself.
#For example, is_prime(11) returns True, and is_prime(9)
#returns False.

#Use the is_prime(n) function to find the first thousand
#prime numbers and display every ten prime numbers in a row,
#as follows:

#2   3   5   7   11   13   17   19   23   29
#31  37  41  43  47   53   59   61   67   71
#73  79  83  89  97  ...
#...

from math import sqrt as sr
def is_prime(n):
    if n==2:
        return True
    if n<2:
        return False
    for i in range(2,int(sr(n)+1)):
        if n%i==0:
            return False
    return True

count=0
num=2
while count!=1000:
    if is_prime(num):
        if count%10==0:
            print()
        print(num,end=" ")
        count+=1
    num+=1
