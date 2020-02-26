import unittest

class StringTest(unittest.TestCase):

    def setUp(self):
        self.s = 'Hello World!'

    def testLen(self):
        self.assertEqual(12, len(self.s))

    def testSlice(self):
        actual = self.s[6:11]
        expected = 'World'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()