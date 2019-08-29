##1. For the calculator program, create an dec2bin and test for 
##decimal to binary conversion.

def check_digit (num):
    if not str(num).isdigit():
        # print("Expected a number.")
        return False
    return True

class Calculator:

    def operation (self, a, b, sign):
        validated = True
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            result = "Expected a number."
            validated = False

        if validated:
            result = 0
            if sign == "*":
                result = a*b
            elif sign == "+":
                result = a+b
            elif sign == "-":
                result = a-b
            elif sign == "/":
                if b == 0:
                    result = "Divide by zero error."
                else:
                    result = a/b
            
        # print(str(a), sign, str(b), "=", str(result))
        return result


    def add (self, a, b):
        result = self.operation(a, b, "+")
        return result


    def subtract (self, a, b):
        result = self.operation(a, b, "-")
        return result


    def multiply (self, a, b):
        result = self.operation(a, b, "*")
        return result


    def divide (self, a, b):
        result = self.operation(a, b, "/")
        return result


    def dec2bin (self, dec):
        # print("Decimal:", str(dec))
        binary = ""
        while dec >= 1:
            binary += str(dec%2)
            dec //= 2
        # print("Binary:", binary[::-1])
        return int(binary[::-1])
