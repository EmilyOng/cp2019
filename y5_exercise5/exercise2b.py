'''
Write a program with the following menu structure:

1. Search
2. Add
3. Update
4. Remove
0. Quit

Implement the respective CRUD operations.
C - create / insert / add
R - read / select / retrieve / display / show
U - update / edit / modify
D - delete / remove / drop
'''
#DBBrowser

import sqlite3
connection=sqlite3.connect("student_database.sqlite")
cursor=connection.cursor()
headers=["Search","Add","Update","Remove","Display All","Quit"]
information=["Index number: ","Name: ","Class: ","Gender: ", "DOB: ","Weight: ","Height: "]
spacing_size=20
cursor.execute("CREATE TABLE IF NOT EXISTS student_database (sid INTEGER, name TEXT, class TEXT, gender TEXT, dob TEXT, weight FLOAT, height FLOAT);")

def validator(val):
    if len(val)==0:
        print("Please enter a valid input.")
        return True

def display_menu():
    print("CRUD")
    print("-"*17)
    for i in range(len(headers)):
        print("|"+"("+str(i+1)+") "+headers[i]+(" "*int((12-len(headers[i]))))+"|")
    print("-"*17)

def search():
    print("SEARCHING FOR STUDENT ")
    print("-"*spacing_size)
    _name=raw_input("Who would you like to search for? ")
    cursor.execute("SELECT * from student_database")
    results=cursor.fetchall()
    found=False
    for result in results:
        if result[1]==_name:
            found=True
            for i in range(len(information)):
                print(information[i]+str(result[i]))
            break
    if not found:
        print("Student "+_name+" is not found in the school's database.")
    else:
        print("Search action has been completed successfully")
        connection.commit()
    try_again=raw_input("Would you like to search for another student? [Y/N] ")
    if try_again=='Y':
        search()

def add():
    print("ADDING A  STUDENT ")
    print("-"*spacing_size)
    _sid=raw_input("Index number: ")
    _name=raw_input("Name: ")
    _class=raw_input("Class: ")
    _gender=raw_input("Gender M/F: ")
    _dob=raw_input("DOB DD/MM/YYYY: ")
    _weight=raw_input("Weight in kg: ")
    _height=raw_input("Height in m: ")
    cursor.execute("INSERT INTO student_database (sid, name, class, gender, dob, weight, height) VALUES (?,?,?,?,?,?,?)", (_sid, _name, _class, _gender, _dob, _weight, _height))
    print("Added student "+_name+" successfully.")
    print("-"*spacing_size)
    connection.commit()
    cursor.execute("SELECT * FROM student_database")
    result=cursor.fetchall()
    result=result[len(result)-1]
    for i in range(len(information)):
        print(information[i]+str(result[i]))
    try_again=raw_input("Would you like to add another student? [Y/N] ")
    if try_again=='Y':
        add()

def update():
    print("UPDATING STUDENT DATABASE")
    print("-"*spacing_size)
    _name=raw_input("Who would you like to update? ")
    cursor.execute("SELECT * FROM student_database")
    results=cursor.fetchall()
    found=False
    for result in results:
        if result[1]==_name:
            found=True
            break
    if not found:
        print("Student "+_name+" is not found in the school's database.")
    else:
        print("What would you like to update?")
        for i in range(len(information)):
            print(information[i]+"("+str(i+1)+")")
        option=int(raw_input("Please select an option: "))
        cursor.execute("SELECT * FROM student_database")
        if option==1:
            new_index_number=int(raw_input("Updated Index Number: "))
            cursor.execute("UPDATE student_database SET sid=? WHERE name=?",[new_index_number,_name])
        elif option==2:
            new_name=raw_input("Updated Name: ")
            cursor.execute("UPDATE student_database SET name=? WHERE name=?",[new_name,_name])
        elif option==3:
            new_class=raw_input("Updated Class: ")
            cursor.execute("UPDATE student_database SET class=? WHERE name=?",[new_class,_name])
        elif option==4:
            new_gender=raw_input("Updated Gender M/F: ")
            cursor.execute("UPDATE student_database SET gender=? WHERE name=?",[new_gender,_name])
        elif option==5:
            new_dob=raw_input("Updated DOB DD/MM/YYYY: ")
            cursor.execute("UPDATE student_database SET dob=? WHERE name=?",[new_dob,_name])
        elif option==6:
            new_weight=float(raw_input("Updated Weight in kg: "))
            cursor.execute("UPDATE student_database SET weight=? WHERE name=?",[new_weight,_name])
        else:
            new_height=float(raw_input("Updated Height in m: "))
            cursor.execute("UPDATE student_database SET height=? WHERE name=?",[new_height,_name])
        print("Updated student "+_name+" successfully.")
        print("-"*spacing_size)
        connection.commit()
        cursor.execute("SELECT * FROM student_database")
        results=cursor.fetchall()
        for result in results:
            if result[1]==_name:
                for i in range(len(information)):
                    print(information[i]+str(result[i]))
                break

    try_again=raw_input("Would you like to update for another student? [Y/N] ")
    if try_again=="Y":
        update()

def remove():
    print("REMOVING STUDENT FROM DATABASE")
    print("-"*spacing_size)
    _name=raw_input("Who would you like to remove? ")
    cursor.execute("SELECT * FROM student_database")
    results=cursor.fetchall()
    found=False
    for result in results:
        if result[1]==_name:
            found=True
            cursor.execute("DELETE FROM student_database WHERE name=?",[_name])
            print("Removed student "+_name+" successfully.")
            print("-"*spacing_size)
            connection.commit()
            break

    if not found:
        print("Student "+_name+" is not found.")
    try_again=raw_input("Would you like to remove another student? [Y/N] ")
    if try_again=="Y":
        remove()

def display_all():
    cursor.execute("SELECT * from student_database")
    results=cursor.fetchall()
    for result in results:
        for i in range(len(information)):
            print(information[i]+str(result[i]))
        print("\n")

display_menu()
option=int(raw_input("What would you like to do? "))
while option!=6:
    if option==1:
        search()
    elif option==2:
        add()
    elif option==3:
        update()
    elif option==4:
        remove()
    else:
        display_all()

    display_menu()
    option=int(raw_input("What would you like to do? "))

connection.commit()
connection.close()
