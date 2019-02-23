#5 (Finding the number of days in a month) q05_find_month_days.py 
#Write a program that prompts the user to enter the month and year,
#and displays the number of days in the month. For example, if the user
#entered month 2 and year 2000, the program should display that
#February 2000 has 29 days. If the user entered month 3 and year 2005,
#the program should display that March 2005 has 31 days.

def determine_leap_year(yr):
    if (yr%4==0 and yr%100!=0) or (yr%400==0):
        return True
    else:
        return False
        
def find_month_days(mth, yr):
    months=["January","February","March","April",
            "May","June","July","August","September",
            "October","November","December"]
    if mth==2:
        if determine_leap_year(yr):
            print("{0} {1} {2}".format("February",yr,"has 29 days."))
        else:
            print("{0} {1} {2}".format("February",yr,"has 28 days."))
    else:
        if mth%2==0:
            print("{0} {1} {2} {3}".format(months[mth-1],yr,"has","31 days."))
        else:
            print("{0} {1} {2} {3}".format(months[mth-1],yr,"has","31 days."))

month=int(input("Enter month: "))
year=int(input("Enter year: "))
find_month_days(month,year)
            
