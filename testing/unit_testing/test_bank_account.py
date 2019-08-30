from bank_account import check_digit, BankAccount
import unittest

class TestBankAccount (unittest.TestCase):

    def setUp (self):
        self.bank = BankAccount("C34")


    def test_nan (self):
        self.assertEqual(self.bank.deposit("a"), "Expected a number.")


    def test_deposit_neg (self):
        self.assertEqual(self.bank.deposit(-1), "Expected a deposition amount more than 0 dollars.")


    def test_deposit (self):
        self.assertEqual(self.bank.deposit(10), 10)


    def test_withdraw_neg (self):
        self.assertEqual(self.bank.withdraw(-1), "Expected a withdrawal amount more than 0 dollars.")
        

    def test_withdraw_morethan (self):
        self.assertEqual(self.bank.withdraw(10000), "Cannot withdrawl an amount more than your current balance.")


    def test_withdraw (self):
        self.bank.deposit(10)
        self.assertEqual(self.bank.withdraw(7), 3)


    def test_calc_interest (self):
        self.bank.deposit(3)
        self.assertEqual(self.bank.calc_interest(2), 3 * ((1.02)**2))


    def test_calc_interest_year (self):
        self.bank.deposit(3)
        self.assertEqual(self.bank.calc_interest(-1), "Expected at least 1 year.")


    def tearDown (self):
        self.bank = None


if __name__ == "__main__":
    unittest.main(exit=False)
