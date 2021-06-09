import unittest

from hex_string import operation, ValidationError


class HexNumberTest(unittest.TestCase):

    def testValidHexString(self):
        self.assertEqual(0xaa, int('AA', 16))

    def testInValidHexString(self):
        with self.assertRaises(ValueError):
            int('AG', 16)

    def testValidData(self):
        self.assertEqual(0xaa, operation('AA'))
        self.assertEqual(0xff, operation('FF'))
        self.assertEqual(0xaaaa, operation('AAAA'))
        self.assertEqual(0xffff, operation('FFFF'))

    def testInValidData_TooShort1(self):
        with self.assertRaises(ValidationError):
            operation('A')

    def testInValidData_TooShort2(self):
        with self.assertRaises(ValidationError):
            operation('F')

    def testInValidData_TooShort3(self):
        with self.assertRaises(ValidationError):
            operation('0')

    def testInValidData_TooShort4(self):
        with self.assertRaises(ValidationError):
            operation('9')

    def testInValidData_TooLong1(self):
        with self.assertRaises(ValidationError):
            operation('AAAAA')

    def testInValidData_TooLong2(self):
        with self.assertRaises(ValidationError):
            operation('FFFFF')

    def testInValidData_TooLong3(self):
        with self.assertRaises(ValidationError):
            operation('00000')

    def testInValidData_TooLong4(self):
        with self.assertRaises(ValidationError):
            operation('99999')

    def testInValidData_TooSmallAsciiCode1(self):
        with self.assertRaises(ValidationError):
            operation('@@')

    def testInValidData_TooSmallAsciiCode2(self):
        with self.assertRaises(ValidationError):
            operation('//')

    def testInValidData_TooLargeAsciiCode1(self):
        with self.assertRaises(ValidationError):
            operation('GG')

    def testInValidData_TooLargeAsciiCode2(self):
        with self.assertRaises(ValidationError):
            operation('::')


if __name__ == '__main__':
    unittest.main()
