import unittest

from basics.ElectronicParts import Resistor


class ResistorTest(unittest.TestCase):


    def testClassVariable(self):
        self.assertEqual('Conrad', Resistor.vendor)


    def testInstanceVariables(self):
        r = Resistor(1000)

        self.assertEqual(1000, r.value)
        self.assertEqual(2, r.tolerance)


    def testChangeDefaultValue(self):
        r = Resistor(470)
        r.tolerance = 5

        self.assertEqual(470, r.value)
        self.assertEqual(5, r.tolerance)


    def testAccessorMethods(self):
        r = Resistor(1000)

        self.assertEqual(1000, r.getValue())
        self.assertEqual(2, r.getTolerance())

    def testAdd(self):
        r1 = Resistor(1000)
        r2 = Resistor(330)
        r1.add(r2)

        self.assertEqual(1000+330, r1.getValue())
        self.assertEqual(2, r1.getTolerance())


if __name__ == '__main__':
    unittest.main()