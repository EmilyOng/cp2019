#12 (Finding the factors of an integer)  q12_find_factors.py
#Write a program that reads an integer and displays all its
#smallest factors. For example, if the input integer is 120,
#the output should be as follows: 2, 2, 2, 3, 5.

from math import sqrt as sr
def find_factors(num):
    step=2
    for i in range(step,int(sr(num)+1)):
        if num%step==0:
            while num%step==0:
                num/=step
                print(step,end=" ")
        step+=1

num=int(input("Number: "))
find_factors(num)
