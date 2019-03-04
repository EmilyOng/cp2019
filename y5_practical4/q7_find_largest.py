#7 (Finding the largest number in an array) q7_find_largest.py
#Write a recursive function find_largest(alist) that returns
#the largest integer in an array alist.  

#For example, given alist = [5, 1, 8, 7, 2], find_largest(alist) returns 8.

def find_largest(alist):
    if len(alist)==1:
        return alist[0]
    if alist[0]>=alist[1]:
        alist.remove(alist[1])
    else:
        alist.remove(alist[0])
    return find_largest(alist)

print(find_largest([5,1,8,7,2]))
