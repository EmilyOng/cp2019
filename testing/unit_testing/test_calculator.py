from calculator import check_digit, Calculator
import unittest

class CalculatorTest (unittest.TestCase):
    
    def setUp (self):
        self.calculator = Calculator()

    def test_add (self):        
        self.assertEqual(self.calculator.add(9, 10), 9+10)


    def test_data_type (self):
        self.assertEqual(self.calculator.add("e", 10), "Expected a number.")

        
    def test_subtract (self):        
        self.assertEqual(self.calculator.subtract(15, 10), 15-10)


    def test_multiply (self):        
        self.assertEqual(self.calculator.multiply(8, -2), 8*-2)


    def test_divide (self):        
        self.assertEqual(self.calculator.divide(9, 2), 9/2)


    def test_divide_by_zero (self):
        self.assertEqual(self.calculator.divide(9, 0), "Divide by zero error.")
        
        
    def test_dec2bin (self):
        self.assertEqual(self.calculator.dec2bin(34), 100010)


    def tearDown (self):
        self.calculator = None
        

if __name__ == "__main__":
    unittest.main(exit=False)
