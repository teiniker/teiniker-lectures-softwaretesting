import unittest

# Sometimes you’ll want to create a list of items that cannot change.
# Tuples allow you to do just that.
# Python refers to values that cannot change as immutable, and an
# immutable list is called a tuple.

# A tuple looks just like a list except you use parentheses instead of
# square brackets. Once you define a tuple, you can access individual
# elements by using each item’s index, just as you would for a list.

class TupleTest(unittest.TestCase):

    immutableList = ()

    def setUp(self):
        self.immutableList = ('homer', 'marge', 'bart')

    # We access each element in the tuple individually, using the same syntax
    # we’ve been using to access elements in a list
    def testTupleIndex(self):
        self.assertEqual('marge', self.immutableList[1])
        self.assertEqual('bart', self.immutableList[-1])

if __name__ == '__main__':  # Command line test runner
    unittest.main()
