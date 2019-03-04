#3 (Computing greatest common divisor using recursion) q3_find_gcd.py
#The greatest common divisor (GCD) of two positive integers m and n,
#gcd(m, n) can be defined recursively as follows: 

#If m % n is 0, gcd(m, n) is n.
#Otherwise, gcd(m, n) is gcd(n, m % n).

#Write a recursive function gcd(m, n) to find the GCD.
#Write a test program that computes gcd(24, 16) and gcd(255, 25).

def gcd(m,n):
    if m%n==0:
        return n
    return gcd(n,m%n)

print(gcd(24,16))
print(gcd(255,25))
