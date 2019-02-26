#2 (Displaying patterns) q2_display_pattern.py
#Write a function display_pattern(n) to display a pattern as follows:
#              1
#            2 1
#          3 2 1
#...
#n n-1 ... 3 2 1

def display_pattern(n):
    for i in range(n):
        for j in range(0,n-i-1):
            print(" ",end="")
        for k in range(n-i-1,n):
            print("*",end="")
        print()
        
display_pattern(5)
            
