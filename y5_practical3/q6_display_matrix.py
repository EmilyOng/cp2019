#6 (Displaying matrix of 0s and 1s) q7_display_matrix.py
#Write a function print_matrix(n) that displays an n by n
#matrix, where n is a positive integer entered by the user.
#Each element is 0 or 1, which is generated randomly. A 3
#by 3 matrix may look like this:

#0 1 0
#0 0 0
#1 1 1

import random
def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print(random.randint(0,1),end=" ")
        print()

print_matrix(3)

