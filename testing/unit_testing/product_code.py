##Write a product code validation program with unit testing.
##The product code should be of 5 characters with first character
##an uppercase letter and the next 4 characters digits in the 
##range 0001 to 9999.

def product_code (code):
    if len(str(code)) != 5:
        return "Product code should be of 5 characters."
    if not 65<=ord(str(code[0]))<=90:
        return "First character should be an uppercase letter."
    num = code[1:]
    try:
        num = int(num)
    except ValueError:
        return "Last 4 characters should be numbers."
    if num==0:
        return "Last 4 characters should be in range 0001 to 9999."

    return "Valid."
