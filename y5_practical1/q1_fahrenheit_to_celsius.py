#1. (Converting Fahrenheit to Celsius)
#Write a program q1_fahrenheit_to_celsius.py
#that reads a Fahrenheit degree in double
#(floating point / decimal) from standard input,
#then converts it to Celsius and displays the
#result in standard output. The formula for the
#conversion is as follows: celsius = (5/9) * (fahrenheit - 32)

def fahrenheit_to_celsius(f):
    celcius=(5/9)*(f-32)
    return celcius
fahrenheit=float(input("Fahrenheit degree: "))
print("{0} {1:.1f}".format("Celcius degree: ",fahrenheit_to_celsius(fahrenheit)))
