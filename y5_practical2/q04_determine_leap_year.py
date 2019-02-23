#4 (Determining leap year) q04_determine_leap_year.py
#Write a program that prompts the user to enter a year
#and determines whether it is a leap year. A year is a
#leap year if it is divisible by 4 but not 100, or is
#divisible by 400. 

def determine_leap_year(num):
    if (num%4==0 and num%100!=0) or (num%400==0):
        print("Leap")
    else:
        print("Non-Leap")

year=int(input("Enter year: "))
determine_leap_year(year)
