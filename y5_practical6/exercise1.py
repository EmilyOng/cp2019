##Write a program to generate today's date and format the date in the following format:
##DD-MM-YYYY
##DDMMYY
##YYMMDD
##<day of week> day month year in full eg Saturday 12 March 2011
##<day of week> day month year in short eg Sat 12 Mar 2011

import datetime as dt

def format_date(format_type):
    date=dt.date.today()
    if format_type=="DD-MM-YYYY":
        print(date.strftime("%d-%m-%Y"))
    elif format_type=="DDMMYY":
        print(date.strftime("%d-%m-%y"))
    elif format_type=="YYMMDD":
        print(date.strftime("%y-%m-%d"))
    elif format_type=="full":
        print(date.strftime("%A %d %B %Y"))
    else:
        print(date.strftime("%a %d %b %Y"))
        
format_type=str(input())
print(format_date(format_type))
