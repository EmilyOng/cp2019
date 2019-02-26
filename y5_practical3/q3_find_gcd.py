#3 (Computing GCD) q3_find_gcd.py
#Write a function gcd(m, n) that returns the greatest common
#divisor between two positive integers:

#Write a test program that computes gcd(24, 16) and gcd(255, 25).

def gcd(m,n):
    if n==0:
        print(m)
    else:
        return gcd(n,m%n)

gcd(24,16)
gcd(255,25)
