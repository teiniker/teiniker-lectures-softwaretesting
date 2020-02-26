import unittest

def setUpModule():
    print('setUpModule()')

def tearDownModule():
    print('tearDownModule()')

class SimpleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass()')

    def setUp(self):
        print('setUp()')

    def tearDown(self):
        print('tearDown()')

    def testA(self):
        print('testA()')

    def testB(self):
        print('testB()')

    @unittest.skip("demonstrating skipping")
    def testC(self):
        print('testC()')
        self.fail()


if __name__ == '__main__':
    unittest.main()