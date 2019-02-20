#5 (Converting an uppercase letter to lowercase)
#Write a program q5_upper_to_lower.py that converts
#an uppercase letter from standard input to a lowercase
#letter by making use of its ASCII value.

def upper_to_lower(char):
   return chr(ord(char)+32)
letter=input("Uppercase: ")
print("Lowercase: ",upper_to_lower(letter))
