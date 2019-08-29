# 3. Refactor age validation to use unit testing.
def manual_testing ():
    valid_age = False
    age = input("Enter your age: ")

    while not valid_age:
        try:
            age = int(age)
        except ValueError:
            print("Expected a number.")
        else:
            if age < 0 or age > 100:
                print("Expected an age from 0 to 100")
            else:
                valid_age = True
                break

        age = input("Enter your age: ")

def validate_age (age):
    if len(str(age)) == 0:
        return "Expected an input."
    try:
        age = int(age)
    except ValueError:
        return "Expected a number."
    if not 1<=age<=90:
        return "Expected an age from 1 to 90."
    return True
