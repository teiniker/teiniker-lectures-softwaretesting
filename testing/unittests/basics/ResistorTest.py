import unittest

from unittests.basics.ElectronicParts import Resistor

class ResistorTest(unittest.TestCase):

    def testClassVariable(self):
        self.assertEqual('Conrad', Resistor.vendor)


    def testResistor(self):
        r = Resistor(470)
        r.tolerance = 5

        self.assertEqual(470, r.value)
        self.assertEqual(5, r.tolerance)


    def testDefaultValue(self):
        r = Resistor(1000)

        self.assertEqual(1000, r.getValue())
        self.assertEqual(2, r.getTolerance())


    def testAddTwoResistors(self):
        r1 = Resistor(1000)
        r2 = Resistor(330)
        r1.add(r2)

        self.assertEqual(1000+330, r1.getValue())


if __name__ == '__main__':
    unittest.main()