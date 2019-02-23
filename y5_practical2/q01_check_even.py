#1 (Checking whether a number is even) q01_check_even.py
#Write a program that reads an integer and checks
#whether it is even. 

def check_even(num):
    if num%2==0:
        print("{0} {1}".format(num, "is even"))
    else:
        print("{0} {1}".format(num, "is odd"))

number=int(input("Enter number: "))
check_even(number)
