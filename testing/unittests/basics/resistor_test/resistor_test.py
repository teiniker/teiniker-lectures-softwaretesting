import unittest

from resistor import Resistor

class ResistorTest(unittest.TestCase):

    def test_class_variable(self):
        self.assertEqual('Neuhold Electronics', Resistor.vendor)


    def test_resistor_init(self):
        # Setup
        res = Resistor(470, 5)
        # Exercise
        # Verify
        self.assertEqual(470, res.value)
        self.assertEqual(5, res.tolerance)
        # Teardown

    def test_default_value(self):
        # Setup
        res = Resistor(1000)
        self.assertEqual(1000, res.value)
        self.assertEqual(2, res.tolerance)


    def test_add_resistors(self):
        res_1 = Resistor(1000)
        res_2 = Resistor(330)
        res = res_1 + res_2
        self.assertEqual(1000+330, res.value)

if __name__ == '__main__':
    unittest.main()
