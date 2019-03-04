#A phone book stores names with their contact numbers.
#Write a phone book application which will allow you to
#search for an entry
#insert an entry
#update an entry 
#delete an entry
#display all entries
#quit
#Your program should continue until the user chooses to quit.

#Assume that one name is only associated with one contact number.

'''
Phone Book Application
'''

phone_book=dict()

def search_entry(entry_key):
    print("SEARCH")
    if entry_key in phone_book:
        print(entry_key+":",phone_book[entry_key])
        return
    else:
        print("User "+entry_key+" is not found, would you like to try again?")
        try_again=input("[Y/N]")
        if try_again=='Y':
            new_entry_key=input("Who do you want to search for?")
            search_entry(new_entry_key)
        else:
            display_menu()
            return

def insert_entry(entry_key,entry_value):
    print("INSERT")
    if entry_key in phone_book:
        print("User "+entry_key+" already exists, would you like to try again?")
        try_again=input("[Y/N]")
        if try_again=='Y':
            new_entry_key=input("Name: ")
            new_entry_value=int(input("Number: "))
            insert_entry(new_entry_key,new_entry_value)
        else:
            display_menu()
            return
    else:
        phone_book[entry_key]=entry_value
        print("Inserted new user "+entry_key+" with number",entry_value)
        return

def update_entry(entry_key,entry_value):
    print("UPDATE")
    if entry_key in phone_book:
        phone_book[entry_key]=entry_value
        print("Updated user "+entry_key+" with number",entry_value)
    else:
        print("User "+entry_key+" is not found, would you like to try again?")
        try_again=input("[Y/N]")
        if try_again=='Y':
            new_entry_key=input("Name: ")
            new_entry_value=int(input("New number: "))
            update_entry(new_entry_key,new_entry_value)
        else:
            display_menu()
            return

def delete_entry(entry_key):
    print("DELETE")
    if entry_key in phone_book:
        phone_book.pop(entry_key)
        print("Deleted user "+entry_key)
        return
    else:
        print("User "+entry_key+" is not found, would you like to try again?")
        try_again=input("[Y/N]")
        if try_again=='Y':
            new_entry_key=input("Name: ")
            delete_entry(new_entry_key)
        else:
            display_menu()
            return

def display_entry(entry_key):
    print("DISPLAY ENTRY")
    if entry_key in phone_book:
        print("Name: "+entry_key)
        print("Number:",phone_book[entry_key])
    else:
        print("User "+entry_key+" is not found, would you like to try again?")
        try_again=input("[Y/N]")
        if try_again=='Y':
            new_entry_key=input("Name: ")
            display_entry(new_entry_key)
        else:
            display_menu()
            return

def display_all():
    print("DISPLAY ALL")
    for i in phone_book:
        print("Name: "+i,"\t","Number:",phone_book[i])
    
def display_menu():
    print("APPLICATION")
    options=["Search for a user","Insert new user","Update existing user",
             "Delete existing user","Display existing user", "Display all users",
             "Quit Application"]
    for i in range(len(options)):
        print("("+str(i+1)+")","\t",options[i])
    
display_menu()
option=int(input("What is your option?"))
while option!=7:
    if option==1:
        entry_key=input("Who do you want to search for?")
        search_entry(entry_key)
        display_menu()
        option=int(input("What is your option?"))
    elif option==2:
        entry_key=input("Name: ")
        entry_value=int(input("Number: "))
        insert_entry(entry_key,entry_value)
        display_menu()
        option=int(input("What is your option?"))
    elif option==3:
        entry_key=input("Name: ")
        entry_value=int(input("Number: "))
        update_entry(entry_key,entry_value)
        display_menu()
        option=int(input("What is your option?"))
    elif option==4:
        entry_key=input("Who do you want to delete?")
        delete_entry(entry_key)
        display_menu()
        option=int(input("What is your option?"))
    elif option==5:
        entry_key=input("Who do you want to see?")
        display_entry(entry_key)
        display_menu()
        option=int(input("What is your option?"))
    else:
        display_all()
        display_menu()
        option=int(input("What is your option?"))
