import unittest

from binary_number import operation, ValidationError

# Parameterized Tests
#
# If the logic to set up the test fixture is the same but uses different data,
# we can extract the common fixture setup, exercise SUT, and verify phases of
# the test into a new parameterized test method.
#
# We define very simple test methods for each test, which then call the
# parameterized test and pass in the data required to make this test unique.

class BinaryNumberTest(unittest.TestCase):

    def parameterizedTest(self, expected, input):
        actual = operation(input)
        self.assertEqual(expected, actual)

    def parameterizedTestWithException(self, exception, input):
        try:
            operation(input)
            self.fail()
        except exception:
            pass
        except:
            self.fail('unexpected exception')

    def testValidData1(self):
        self.parameterizedTest(0b0, '0')

    def testValidData2(self):
        self.parameterizedTest(0b1, '1')

    def testValidData3(self):
        self.parameterizedTest(0b0, '00000000')

    def testValidData4(self):
        self.parameterizedTest(0b11111111, '11111111')

    def testInValidData_TooShort(self):
        self.parameterizedTestWithException(ValidationError, '')

    def testInValidData_TooLong1(self):
        self.parameterizedTestWithException(ValidationError, '000000000')

    def testInValidData_TooLong2(self):
        self.parameterizedTestWithException(ValidationError, '111111111')

    def testInValidData_TooSmallAsciiValue(self):
        self.parameterizedTestWithException(ValidationError, '/')

    def testInValidData_TooLargeAsciiValue(self):
        self.parameterizedTestWithException(ValidationError, '2')

if __name__ == '__main__':
    unittest.main()

# References:
# > Parameterized Test
#    http://xunitpatterns.com/Parameterized%20Test.html
# > Python Exception Handling - Try, Except and Finally
#   https://www.programiz.com/python-programming/exception-handling
