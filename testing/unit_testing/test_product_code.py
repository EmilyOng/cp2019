from product_code import product_code
import unittest

class TestProductCode (unittest.TestCase):

    def test_length (self):
        self.assertEqual(product_code("A12345"), "Product code should be of 5 characters.")


    def test_uppercase (self):
        self.assertEqual(product_code("a1234"), "First character should be an uppercase letter.")


    def test_numbers (self):
        self.assertEqual(product_code("Abcde"), "Last 4 characters should be numbers.")


    def test_range (self):
        self.assertEqual(product_code("A0000"), "Last 4 characters should be in range 0001 to 9999.")


    def test_valid (self):
        self.assertEqual(product_code("A1234"), "Valid.")


if __name__ == "__main__":
    unittest.main(exit=False)
