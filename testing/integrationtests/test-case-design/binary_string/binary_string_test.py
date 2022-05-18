import unittest

from binary_string import operation, ValidationError

class BinaryNumberTest(unittest.TestCase):

    def test_valid_binary_string(self):
        value = int('11110000', 2)
        self.assertEqual(240, value)

    def test_invalid_binary_string(self):
        with self.assertRaises(ValueError):
            int('012', 2)

    def test_valid_data(self):
        self.assertEqual(0b0, operation('0'))
        self.assertEqual(0b1, operation('1'))
        self.assertEqual(0b0, operation('00000000'))
        self.assertEqual(0b11111111, operation('11111111'))

    def test_invalid_data_too_short(self):
        with self.assertRaises(ValidationError):
            operation('')

    def test_invalid_data_too_long1(self):
        with self.assertRaises(ValidationError):
            operation('000000000')

    def test_invalid_data_too_long2(self):
        with self.assertRaises(ValidationError):
            operation('111111111')

    def test_invalid_data_too_small_ascii_value(self):
        with self.assertRaises(ValidationError):
            operation('/')

    def test_invalid_data_too_large_ascii_value(self):
        with self.assertRaises(ValidationError):
            operation('2')


if __name__ == '__main__':
    unittest.main()
