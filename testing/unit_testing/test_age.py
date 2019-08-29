import unittest
from age_validation import validate_age

class AgeTest (unittest.TestCase):

    def test_length (self):
        self.assertEqual(validate_age(""), "Expected an input.")


    def test_data_type (self):
        self.assertEqual(validate_age("hlelo"), "Expected a number.")


    def test_range (self):
        self.assertEqual(validate_age(100), "Expected an age from 1 to 90.")


    def test_valid (self):
        self.assertEqual(validate_age(9), True)


if __name__ == "__main__":
    unittest.main(exit=False)
