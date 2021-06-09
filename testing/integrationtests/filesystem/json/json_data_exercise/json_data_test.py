import unittest
import os
import json

class JsonDataTest(unittest.TestCase):

# TODO: Implement setUp() and tearDown()

    def testDeserializationFromFile(self):
        # Exercise
        with open(self.FILE_PATH, "r") as read_file:
            data = json.load(read_file)
        # Verify
        expected = {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}
        self.assertDictEqual(expected, data)

    def testModifyJsonFile(self):
        # Setup
        data = {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}
        # Exercise
        data['person']['age'] = 50
        with open(self.FILE_PATH, "w") as write_file:
            json.dump(data, write_file, indent=2)
        # Verify
        with open(self.FILE_PATH, "r") as read_file:
            data = json.load(read_file)
        expected = {'person': {'name': 'John', 'age': 50, 'city': 'Graz'}}
        self.assertDictEqual(expected, data)

if __name__ == '__main__':
    unittest.main()
