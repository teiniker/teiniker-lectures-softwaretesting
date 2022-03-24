import unittest

class ListTest(unittest.TestCase):
    def setUp(self):
        self.list = ['homer', 'marge', 'bart']

    def testListEqual(self):
        expected = ['homer', 'marge', 'bart']
        self.assertListEqual(expected, self.list)

    def testCountEqual(self):
        expected = ['homer', 'marge', 'bart']
        self.assertCountEqual(expected, self.list)

    def testListIndex(self):
        self.assertEqual('marge', self.list[1])
        self.assertEqual('bart', self.list[-1])

    def testListSize(self):
        actual = len(self.list)
        expected = 3
        self.assertEqual(expected, actual)

    def testListModifyElement(self):
        self.list[2] = 'lisa'
        expected = ['homer', 'marge', 'lisa']
        self.assertEqual(expected, self.list)

    def testListAppend(self):
        self.list.append('lisa')
        expected = ['homer', 'marge', 'bart', 'lisa']
        self.assertEqual(expected, self.list)

    def testListInsert(self):
        self.list.insert(1,'lisa')
        expected = ['homer', 'lisa', 'marge', 'bart']
        self.assertEqual(expected, self.list)

    def testListDeleteElement(self):
        del self.list[1]
        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)

    def testListPop(self):
        s = self.list.pop()
        expected = ['homer', 'marge']
        self.assertEqual(expected, self.list)
        self.assertEqual('bart', s)

    def testListPopWithIndex(self):
        s = self.list.pop(1)
        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)
        self.assertEqual('marge', s)

    def testListRemove(self):
        self.list.remove('homer')
        expected = ['marge', 'bart']
        self.assertEqual(expected, self.list)

    def testListSort(self):
        self.list.sort()
        expected = ['bart', 'homer', 'marge']
        self.assertEqual(expected, self.list)

    def testListReverse(self):
        self.list.reverse()
        expected = ['bart', 'marge', 'homer']
        self.assertEqual(expected, self.list)

    def testListSlice(self):
        slice = self.list[1:2]  # [from:to)
        expected = ['marge']
        self.assertEqual(expected, slice)

    def testListRange(self):
        numList = list(range(3,7))  # [from:to)
        expected = [3, 4, 5, 6]
        self.assertEqual(expected, numList)


if __name__ == '__main__':
    unittest.main()
