import re
valid_gender=False
while not valid_gender:
    gender=input()
    pattern=re.compile("^[mMfF]$")
    if not pattern.match(gender):
        print("Invalid gender")
    else:
        print("Valid gender")
        valid_gender=True
