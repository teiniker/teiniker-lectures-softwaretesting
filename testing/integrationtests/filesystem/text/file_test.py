import unittest

class FileTest(unittest.TestCase):

    def setUp(self):
        # Setup
        self.file = open('Sympathy.txt')

    def tearDown(self):
        # Teardown
        self.file.close()


    def testReadFile(self):
        text = self.file.read()
        print(text)
        self.assertEqual(389, len(text))

    def testReadLines(self):
        lines = self.file.readlines()
        print(lines)
        self.assertEqual(16, len(lines))

    def testReadFileAutoclose(self):
        with open('Sympathy.txt') as f:
            lines = f.readlines()
            print(lines)
            self.assertEqual(16, len(lines))

if __name__ == '__main__':
    unittest.main()


