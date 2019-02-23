#9 (Finding the smallest n such that n2 > 12000) q09_find_smallest.py
#Use a while loop to find the smallest integer n such that n2
#is greater than 12,000. 

from math import sqrt as sr
#n^2>12 000
#(n^2-12000)>0
#(n+sqrt(12000))(n-sqrt(12000)>0
#n<-sqrt(12000) or n>sqrt(12000)
def find_smallest(n,cmp):
    while n>=(-sr(cmp)):
        n-=1
    print(n) 

find_smallest(0,12000)
