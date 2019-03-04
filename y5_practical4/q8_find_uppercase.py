#8 (Finding the number of uppercase letters in a string) q8_find_uppercase.py
#Write a recursive function find_num_uppercase(str) to return the number
#of uppercase letters in a string str.

#For example, find_num_uppercase('Good MorninG!') returns 3.

def find_num_uppercase(str):
    if len(str)==0:
        return 0
    if str[len(str)-2:len(str)-1].isupper():
        return find_num_uppercase(str[:len(str)-1])+1
    else:
        return find_num_uppercase(str[:len(str)-1])

print(find_num_uppercase('Good MorninG!'))
