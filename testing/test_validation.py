import unittest
from age_validation_tdd import validate_age
class TestCases(unittest.TestCase):
    def test_presence(self):
        self.assertEqual(validate_age(''),'Empty input')
    def test_datatype(self):
        self.assertEqual(validate_age('abc'),'Expected a number')
    def test_range(self):
        self.assertEqual(validate_age('999'),'Expected 1-99')
    def test_normal(self):
        self.assertEqual(validate_age('17'),'17')
if __name__=='__main__':
    unittest.main()
