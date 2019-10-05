#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0
for i in range (len(a)):
    swap = False
    for j in range (len(a)-i-1):
        if a[j] > a[j+1]:
            swap = True
            swaps += 1
            a[j], a[j+1] = a[j+1], a[j]
    if not swap:
        break

print("Array is sorted in "+str(swaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]),end="")
