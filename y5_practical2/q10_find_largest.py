#10 (Finding the largest n such that n3<12000)  q10_find_largest.py
#Use a while loop to find the largest integer n such that n3
#is less than 12,000.

def find_largest(n,cmp):
    while n<int(cmp**(1/3)):
        n+=1
    print(n)

find_largest(0,12000)
