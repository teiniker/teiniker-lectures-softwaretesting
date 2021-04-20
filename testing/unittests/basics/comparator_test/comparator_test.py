import unittest

def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


# There are three paths through that compare() function, thus we need
# three test cases to cover all the code.

class ComperatorTest(unittest.TestCase):

    def testAgtB(self):
        # Setup
        # Exercise
        actual = compare(7,3)
        # Verify
        self.assertEqual(1, actual)
        # Teardown

    def testAltB(self):
        # Setup
        # Exercise
        actual = compare(3,7)
        # Verify
        self.assertEqual(-1, actual)
        # Teardown

    def testAeqB(self):
        # Setup
        # Exercise
        actual = compare(7,7)
        # Verify
        self.assertEqual(0, actual)
        # Teardown

if __name__ == '__main__':
    unittest.main()