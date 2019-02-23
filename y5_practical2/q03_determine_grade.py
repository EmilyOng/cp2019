#3 (Determining grade) q03_determine_grade.py
#Write a program that prompts the user to enter a
#score between 0 and 100 inclusive. The grading system is as follows:
#A: 70 - 100
#B: 60 - 69
#C: 55 - 59
#D: 50 - 54
#E: 45 - 49
#S: 35 - 44
#U: 0 - 34

def determine_grade(grade):
    if grade<0 or grade>100:
        print("Invalid! Score must be within 0 - 100.")
    elif grade>=70:
        print("A")
    elif grade>=60:
        print("B")
    elif grade>=55:
        print("C")
    elif grade>=50:
        print("D")
    elif grade>=45:
        print("E")
    elif grade>=35:
        print("S")
    else:
        print("U")

score=int(input("Enter score: "))
determine_grade(score)
