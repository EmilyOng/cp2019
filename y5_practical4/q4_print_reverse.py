#4 (Reverse the digits in an integer recursively) q4_print_reverse.py
#Write a recursive function reverse_int(n) that reverses the digits
#of an integer n: 

#For example, reverse_int(12345) displays 54321.

def reverse_int(n):
    n=str(n)
    if len(n)==0:
        return n[len(n)-1:len(n)]
    return n[len(n)-1:len(n)]+reverse_int(n[:len(n)-1])

print(reverse_int(849798),end="")
