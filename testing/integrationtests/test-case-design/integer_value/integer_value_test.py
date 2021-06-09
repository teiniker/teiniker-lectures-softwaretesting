import unittest

from integer_value import operation, ValidationError

# Boundary Value Analysis:
#   Valid numbers: 1, 99
#   Invalid numbers: 0, 100

class IntegerValueTest(unittest.TestCase):

    def testValidNumbers(self):       
        self.assertEqual(1, operation(1))
        self.assertEqual(99, operation(99))

    def testInValid_TooSmall(self):
        with self.assertRaises(ValidationError):
            operation(0)

    def testInValid_TooLarge(self):
        with self.assertRaises(ValidationError):
            operation(100)


if __name__ == '__main__':
    unittest.main()
