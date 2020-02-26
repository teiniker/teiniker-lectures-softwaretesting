import unittest

# A list is a collection of items in a particular order.
# You can put anything you want into a list, and the items in your list don’t
# have to be related in any particular way.
# Square brackets ([]) indicate a list, and individual elements in the list are
# separated by commas.

class ListTest(unittest.TestCase):

    list = []

    # We can factor out set-up code by implementing a method called setUp(),
    # which the testing framework will automatically call for every single
    # test we run:
    def setUp(self):
        self.list = ['homer', 'marge', 'bart']


    # assertListEqual(first, second, msg=None)
    # Tests that two lists or tuples are equal.
    # If not, an error message is constructed that shows only the differences
    # between the two. An error is also raised if either of the parameters
    # are of the wrong type.
    # These methods are used by default when comparing lists or tuples with
    # assertEqual().
    def testListEqual(self):
        expected = ['homer', 'marge', 'bart']
        self.assertListEqual(expected, self.list)


    # assertCountEqual(first, second, msg=None)¶
    # First and second have the same elements in the same number, regardless of their order.
    def testCountEqual(self):
        expected = ['homer', 'marge', 'bart']
        self.assertCountEqual(expected, self.list)


    # To access an element in a list, write the name of the list followed
    # by the index of the item enclosed in square brackets.
    # By asking for the item at index -1, Python always returns the last
    # item in the list.
    def testListIndex(self):
        self.assertEqual('marge', self.list[1])
        self.assertEqual('bart', self.list[-1])


    # len() returns the length of a list
    def testListSize(self):
        self.assertEqual(3, len(self.list))

    # To change an element, use the name of the list followed by the index of
    # the element you want to change, and then provide the new value you want
    # that item to have.
    def testListModifyElement(self):
        self.list[2] = 'lisa'

        expected = ['homer', 'marge', 'lisa']
        self.assertEqual(expected, self.list)

    # The simplest way to add a new element to a list is to append the item
    # to the list.
    def testListAppend(self):
        self.list.append('lisa')

        expected = ['homer', 'marge', 'bart', 'lisa']
        self.assertEqual(expected, self.list)


    # You can add a new element at any position in your list by using the
    # insert() method. You do this by specifying the index of the new element
    # and the value of the new item.
    def testListInsert(self):
        self.list.insert(1,'lisa')

        expected = ['homer', 'lisa', 'marge', 'bart']
        self.assertEqual(expected, self.list)


    # If you know the position of the item you want to remove from a list,
    # you can use the del statement.
    def testListDeleteElement(self):
        del self.list[1]

        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)

    # The pop() method removes the last item in a list, but it lets you work
    # with that item after removing it.
    def testListPop(self):
        s = self.list.pop()

        expected = ['homer', 'marge']
        self.assertEqual(expected, self.list)
        self.assertEqual('bart', s)


    # You can actually use pop() to remove an item in a list at any position
    # by including the index of the item you want to remove in parentheses.
    def testListPopWithIndex(self):
        s = self.list.pop(1)

        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)
        self.assertEqual('marge', s)


    # If you only know the value of the item you want to remove, you can use
    # the remove() method.
    # The remove() method deletes only the first occurrence of the value you
    # specify. If there’s a possibility the value appears more than once in
    # the list, you’ll need to use a loop to determine if all occurrences of
    # the value have been removed.
    def testListRemove(self):
        self.list.remove('homer')

        expected = ['marge', 'bart']
        self.assertEqual(expected, self.list)


    # The sort() method changes the order of the list permanently.
    # The sorted() function can also accept a reverse=True argument if you
    # want to display a list in reverse alphabetical order.
    def testListSort(self):
        self.list.sort()

        expected = ['bart', 'homer', 'marge']
        self.assertEqual(expected, self.list)


    # To reverse the original order of a list, we can use the reverse() method.
    def testListReverse(self):
        self.list.reverse()

        expected = ['bart', 'marge', 'homer']
        self.assertEqual(expected, self.list)


    # To make a slice, you specify the index of the first and last elements
    # you want to work with.
    def testListSlice(self):
        slice = self.list[1:2]  # [from:to)

        expected = ['marge']
        self.assertEqual(expected, slice)

        slice[0] = 'moe'
        print(self.list)    # slice creates a copy


    # When you wrap list() around a call to the range() function, the output
    # will be a list of numbers.
    def testListRange(self):
        numList = list(range(3,7))  # [from:to)

        expected = [3, 4, 5, 6]
        self.assertEqual(expected, numList)


if __name__ == '__main__':
    unittest.main()
