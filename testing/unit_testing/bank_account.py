##2. For the bank account program, create a class method calc_interest that
##compute the total balance after n years with an interest rate of 2% per annum.

def check_digit (num):
    if not str(num).isdigit():
        print("Expected a number.")
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
            return False
        if num <= 0:
            print("Expected a deposition amount more than 0 dollars.")
            return False

        self.bank += num
        self.update_account()


    def withdraw (self, num):
        if not check_digit(num):
            return False
        if num <= 0:
            print("Expected a withdrawal amount more than 0 dollars.")
            return False
        if num > self.bank:
            print("Cannot withdrawl an amount more than your current balance.")
            return False

        self.bank -= num
        self.update_account()


    def see_account (self):
        self.update_account("Current")


# main
bank = BankAccount("C34")
bank.withdraw(10)
bank.deposit(100)
bank.see_account()
    
