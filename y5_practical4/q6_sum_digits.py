#6 (Summing the digits in an integer using recursion) 
#Write a recursive function sum_digits(n) that computes
#the sum of the digits in an integer n: 

#For example, sum_digits(234) returns 9.

def sum_digits(n):
    n=str(n)
    if len(n)==0:
        return 0
    return sum_digits(n[:len(n)-1])+int(n[len(n)-1:len(n)])

print(sum_digits(234))
