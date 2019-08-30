##2. For the bank account program, create a class method calc_interest that
##compute the total balance after n years with an interest rate of 2% per annum.

def check_digit (num):
    try:
        num = int(num)
    except ValueError:
        return False
    return True


class BankAccount:

    def __init__ (self, account_number):
        self.bank = 0
        self.account_number = str(account_number)


    def update_account (self, update="New"):
        print(update, "balance for", self.account_number, "is", str(self.bank))


    def deposit (self, num):
        if not check_digit(num):
            return "Expected a number."
        if num <= 0:
            return "Expected a deposition amount more than 0 dollars."

        self.bank += num
##        self.update_account()
        return self.bank


    def withdraw (self, num):
        if not check_digit(num):
            return "Expected a number."
        if num <= 0:
            return "Expected a withdrawal amount more than 0 dollars."
        if num > self.bank:
            return "Cannot withdrawl an amount more than your current balance."
        
        self.bank -= num
##        self.update_account()
        return self.bank



    def see_account (self):
        self.update_account("Current")


    def calc_interest (self, year):
        if year <= 0:
            return "Expected at least 1 year."
        return self.bank * ((1.02)**year)
    


# main
##bank = BankAccount("C34")
##bank.withdraw(10)
##bank.deposit(100)
##bank.see_account()
##    
