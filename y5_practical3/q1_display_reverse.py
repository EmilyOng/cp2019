#1 (Displaying an integer reversed) q1_display_reverse.py
#Write a function reverse_int(n) to display an integer in
#reverse order:

def reverse_int(n):
    if len(n)==0:
        exit(0)
    print(n[len(n)-1:len(n)],end=" ")
    return reverse_int(n[:len(n)-1])

reverse_int("3456")
