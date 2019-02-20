#4 (Summing the digits in an integer)
#Write a program q4_sum_digits.py that
#reads an integer between 0 and 1000 and
#adds all the digits in the integer. For example,
#if an integer is 932, the sum of all its digits is 14.
#Hint: Use the % operator to extract digits, and use
#the // operator to remove the extracted digit.
#For instance, 932 % 10 = 2 and 932 // 10 = 93 

def get_number(num):
    sum=0
    while(num>0):
        sum+=(num%10)
        num//=10
    return sum

def compute_as_string(num):
    sum1=0
    num_string=str(num)
    for i in num_string:
        sum1+=int(i)
    return sum1

number=int(input("Number: "))
print("Digits Sum: ",get_number(number))
