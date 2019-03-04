#5 (Occurrences of a specified character in a string) q5_count_letter.py
#Write a recursive function count_letter(str, ch) that finds the number
#of occurrences of a specified letter ch in a string str: 

#For example, count_letter("Welcome", 'e') returns 2.

def count_letter(str,ch):
    if len(str)==0:
        return 0
    if str[len(str)-1:len(str)]==ch:
        return count_letter(str[:len(str)-1],ch)+1
    else:
        return count_letter(str[:len(str)-1],ch)

print(count_letter("Welcome",'e'))
