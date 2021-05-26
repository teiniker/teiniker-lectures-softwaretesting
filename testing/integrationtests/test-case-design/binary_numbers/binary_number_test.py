import unittest

from binary_number import operation, ValidationError

class BinaryNumberTest(unittest.TestCase):

    def testValidBinaryString(self):
        value = int('11110000', 2)
        self.assertEqual(240, value)

    def testInValidBinaryString(self):
        with self.assertRaises(ValueError):
            int('012', 2)

    def testValidData(self):
        self.assertEqual(0b0, operation('0'))
        self.assertEqual(0b1, operation('1'))
        self.assertEqual(0b0, operation('00000000'))
        self.assertEqual(0b11111111, operation('11111111'))

    def testInValidData_TooShort(self):
        with self.assertRaises(ValidationError):
            operation('')

    def testInValidData_TooLong1(self):
        with self.assertRaises(ValidationError):
            operation('000000000')

    def testInValidData_TooLong2(self):
        with self.assertRaises(ValidationError):
            operation('111111111')

    def testInValidData_TooSmallAsciiValue(self):
        with self.assertRaises(ValidationError):
            operation('/')

    def testInValidData_TooLargeAsciiValue(self):
        with self.assertRaises(ValidationError):
            operation('2')


if __name__ == '__main__':
    unittest.main()
