import unittest

from unittests.basics.ElectronicParts import Resistor

# TODO: Implement the following test cases:
#       > Create in instance of Resistor (470 Ohm, 5%)
#       > Create in instance of Resistor (1000 Ohm)
#         and use the default value for tolerance
#       > Add two Resistor instances of values 1000 and 330 Ohm

class ResistorTest(unittest.TestCase):

    def testClassVariable(self):
        self.assertEqual('Conrad', Resistor.vendor)

if __name__ == '__main__':
    unittest.main()