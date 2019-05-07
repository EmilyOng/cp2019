#task 1.1
import re
def task_1_1_method_1():
    valid_input=False
    while not valid_input:
        letter=str(input("Enter a single letter: "))
        pattern=re.compile("^[a-zA-Z]$")
        if pattern.match(letter):
            print("Correct")
            valid_input=True
        else:
            print("Please enter a single letter")
def task_1_1_method_2():
    valid_input=False
    while not valid_input:
        letter=str(input("Enter a single letter: "))
        if letter.isalpha():
            print("Correct")
            valid_input=True
        else:
            print("Please enter a single letter")

#task 1.2
def task_1_2():
    


    
