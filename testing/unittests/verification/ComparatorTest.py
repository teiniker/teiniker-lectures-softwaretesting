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
        actual = compare(7,3)
        self.assertEqual(1, actual)

    # def testAltB(self):
    #     actual = compare(3,7)
    #     self.assertEqual(-1, actual)
    #
    # def testAeqB(self):
    #     actual = compare(7,7)
    #     self.assertEqual(0, actual)

if __name__ == '__main__':
    unittest.main()

# How to run the code coverage analysis?
# $ coverage3 run - m unittest unittests/basics/ComparatorTest.py
# $ coverage3 report - m
# $ coverage3 html
# Browser: file: ///home/student/github/teiniker-lectures-softwaretesting/htmlcov/index.html
