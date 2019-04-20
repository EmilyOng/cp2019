##The check digit of a Singapore-based NRIC is actually derived from modulo arithmetic
##
##Write a program nric_validation.py to validate a user-input NRIC. Your program should contain
##
##a function to return the check alphabet of a NRIC
##a boolean function to determine if a user-input NRIC is valid
##
##Reference:
##http://coding-and-crypto.tripod.com/01NRIC.htm

import re
weight=[2,7,6,5,4,3,2]
alpha_weight={}
for i in range(9):
    alpha_weight[i+1]=chr(65+i)
alpha_weight[10]=chr(90)
alpha_weight[11]=chr(74)

valid_flag=False

def compare_alphabet(check_digit,nric):
    if alpha_weight[check_digit]==str(nric[-1]).upper():
        return True
    else:
        return False
def valid_nric(nric):
    pattern=re.compile("^[sStT][0-9]{7}[a-zA-Z]$")
    check_valid_nric=bool(pattern.match(nric))
    if not check_valid_nric:
        return False
    total_weight=0
    for digit in range(1,8):
        total_weight+=int(nric[digit])*weight[digit-1]
    remainder=total_weight%11
    check_digit=11-remainder
    print(total_weight,check_digit)
    print(alpha_weight)
    if compare_alphabet(check_digit,nric):
        return True
    else:
        return False
while not valid_flag:
    nric=str(input())
    if not valid_nric(nric):
        print("Please enter a valid NRIC.")
        continue
    valid_flag=True

    

