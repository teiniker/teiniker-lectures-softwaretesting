import unittest

from resistor import Resistor

class ResistorTest(unittest.TestCase):

    def test_class_variable(self):
        self.assertEqual('Neuhold Electronics', Resistor.vendor)


    def test_resistor_init(self):
        # Setup
        r = Resistor(470, 5)
        # Exercise
        # Verify
        self.assertEqual(470, r.value)
        self.assertEqual(5, r.tolerance)
        # Teardown

    def test_default_value(self):
        r = Resistor(1000)
        self.assertEqual(1000, r.value)
        self.assertEqual(2, r.tolerance)


    def test_add_resistors(self):
        # Setup
        r1 = Resistor(1000)
        r2 = Resistor(330)
        # Exercise
        r = r1 + r2
        # Verify
        self.assertEqual(1000+330, r.value)
        # Teardown

if __name__ == '__main__':
    unittest.main()