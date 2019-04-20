valid_age=False
while not valid_age:
    age=input("Age: ")
    try:
        age=int(age)
    except ValueError or TypeError:
        if len(str(age))==0:
            print("Empty input.",end=" ")
        else:
            print("Invalid input.",end=" ")
        print("Enter a valid integer")
    else:
        if 1<=age<=100:
            valid_age=True
        else:
            print("Enter an age from 1 to 100")
