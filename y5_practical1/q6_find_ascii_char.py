#6 (Finding the character of an ASCII code)
#Write a program q6_find_ascii_char.py that
#receives an ASCII code (an integer between 0 and 127)
#and displays its character. For example, if the user
#enters 97, the program displays character a.

def ascii(code):
    return chr(code)
num=int(input("ASCII code: "))
if(num<33):
    print("Control keys from 0-31 and space for 32")
else:
    print("Character: ",ascii(num))
