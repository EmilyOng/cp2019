##Write a program to get a student's nric, name, class, gender,
##date of birth, weight (in kg) and height (in metres).
##Your program should perform the necessary validation.
##Save your program to a file STUDENTS.DAT in append mode
##using the following structure:
##
##<NRIC><name><class><gender><dob><weight><height>
##
##class is in the form <YY>Y<9>C<99> eg 13Y5C23
##name is at most 30 characters
##date of birth is in DD-MM-YYYY format
## 
##sample record:
##S1234567ALim Ah Seng ... M13Y5C23 601.57
##

import nric_validation
import re
from datetime import datetime
attrib=[]
choices=["NRIC","Name","Class","Gender F/M","DOB DD/MM/YYYY",
             "Weight (kg)","Height (m)"]
        
def disp_attrib_setter():
    attrib=[]
    for choice in choices:
        if choice=="NRIC":
            print(choice+": ",end="")
            nric=nric_validation.start()
            attrib.append(nric)
        else:
            valid_input=False
            choice_input=""
            curr_year=str(datetime.now().year)
            curr_year=curr_year[2:4]
            while not valid_input:
                choice_input=input(choice+": ")
                if len(str(choice_input))==0:
                        print("Empty input. Please enter a valid integer.")
                elif choice in ["Weight (kg)", "Height (m)"]:
                    try:
                        choice_input=int(choice_input)
                    except ValueError or TypeError:
                        print("Please enter a valid integer.")
                    else:
                        valid_input=True
                elif choice=="Class":
                    pattern=re.compile(curr_year+"[yY][5-6][cC][1-4][1-8]")
                    if bool(pattern.match(choice_input)):
                        valid_input=True
                    else:
                        print("Please enter a valid class in the form <YY>Y<9>C<99>")
                elif choice=="Gender F/M":
                    pattern=re.compile("^[mMfF]$")
                    if bool(pattern.match(choice_input)):
                        valid_input=True
                    else:
                        print("Please enter F or M")
                elif choice=="DOB DD/MM/YYYY":
                    try:
                        dob_date=int(choice_input[:2])
                        dob_month=int(choice_input[3:5])
                        dob_year=int(choice_input[6:10])
                    except ValueError or TypeError:
                        print("Please enter a DOB in the form DD/MM/YYYY")
                    else:
                        if len(choice_input)!=10:
                            print("Please enter a DOB in the form DD/MM/YYYY")
                            continue
                        if 1900<=dob_year<=int(datetime.now().year):
                            valid_input=True
                        else:
                            print("Please enter a DOB in the form DD/MM/YYYY")
                            continue
                        if dob_month==2:
                            if dob_date<=29:
                                valid_input=True
                            else:
                                print("Please enter a DOB in the form DD/MM/YYYY")
                                continue
                        if dob_month%2==0:
                            if dob_date<=30:
                                valid_input=True
                            else:
                                print("Please enter a DOB in the form DD/MM/YYYY")
                                continue
                        if dob_month%2!=0:
                            if dob_date<=31:
                                valid_input=True
                            else:
                                print("Please enter a DOB in the form DD/MM/YYYY")
                                continue
                else:
                    valid_input=True
            attrib.append(choice_input)
    return attrib

def set_attrib(attrib):
    attrib=attrib
    students_data_infile=open("students_data.txt","a+")
    students_data_infile.write("Data for "+attrib[2]+" "+attrib[1]+"\n")
    for i in range(len(attrib)):
        if i==0:
            students_data_infile.write(choices[i]+": "+"HIDDEN"+"\n")
            continue
        students_data_infile.write(choices[i]+": "+str(attrib[i])+"\n")
    students_data_infile.write("\n")
    students_data_infile.close()
        
def menu():
    print("WELCOME")
    quit_prog=False
    while not quit_prog:
        print("Enter student's verifications:")
        attrib=disp_attrib_setter()
        set_attrib(attrib)
        print("Successfully written to file. Would you like to continue?")
        continue_input=str(input("Y/N "))
        if continue_input in ["N","n"]:
            print("Quitting program...")
            quit_prog=True

menu()
