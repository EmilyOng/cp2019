#Write a program which will create a database school
#with a table students. The students table will store
#the following information about a student: sid, name,
#class, gender, dob, weight (kg) and height (m).

import sqlite3

connection=sqlite3.connect("student_information.sqlite")
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS student_information (sid INTEGER, name TEXT, class TEXT, gender TEXT, dob TEXT, weight FLOAT, height FLOAT);")
print("Student database:")
option=raw_input("Do you want to proceed? [Y/N]")
headers=["Index number: ","Name: ","Class: ","Gender: ","DOB: ","Weight: ","Height: "]
while option=="Y":
    _sid=int(raw_input("Index number: "))
    _name=raw_input("Name: ")
    _class=raw_input("Class: ")
    _gender=raw_input("Gender M/F: ")
    _dob=raw_input("DOB DD/MM/YYYY: ")
    _weight=float(raw_input("Weight in kg: "))
    _height=float(raw_input("Height in m: "))
    cursor.execute("INSERT INTO student_information (sid, name, class, gender, dob, weight, height) VALUES(?,?,?,?,?,?,?)",(_sid,_name,_class,_gender,_dob,_weight,_height))
    cursor.execute("SELECT * from student_information")
    results=cursor.fetchall()
    print("Student database updated for "+_name)
    verification=raw_input("Do you want to verify records? [Y/N]")
    if verification=="Y":
        for i in range(len(headers)):
            print(headers[i]+str(results[len(results)-1][i]))
        print("\n\n")
    check_all=raw_input("Do you want to check all records? [Y/N]")
    if check_all=="Y":
        for result in results:
            for i in range(len(headers)):
                print(headers[i]+str(result[i]))
            print("\n")
        print("\n")
    option=raw_input("Do you want to continue? [Y/N]")
connection.commit()
connection.close()
