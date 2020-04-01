import unittest
import re

# Exercise: Boundary Value Analysis - Hex Numbers
#
# For a given function "operation()" which accepts hex numbers, test cases
# should be implemented. The range of hex numbers is defined by the following
# regular expression: '^[A-F0-9]{2,4}$'
#
# i) Design the minimum set of test cases (based on boundary value analysis)
#
# ii) Implement the test cases in the "HexNumberTest" class.

class ValidationError(Exception):
    pass


def operation(data):
    print(data)
    pattern = '^[A-F0-9]{2,4}$'  # Regular expression
    result = re.match(pattern, data)
    if result:
        return int(data, 16)
    else:
        raise ValidationError('Invalid data value!');


class HexNumberTest(unittest.TestCase):

    def testValidHexString(self):
        value = int('AA', 16)

    def testInValidHexString(self):
        with self.assertRaises(ValueError):
            int('AG', 16)

# TODO: Implement test cases here!

if __name__ == '__main__':
    unittest.main()

