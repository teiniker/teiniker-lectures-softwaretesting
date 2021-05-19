import unittest
import os
import json

class JsonFileTest(unittest.TestCase):
    FILE_PATH = 'data.json'

    def setUp(self):
        data = {'person': {'name': 'John', 'age': 30, 'city': 'Graz'}}
        with open(self.FILE_PATH, "w") as write_file:
            json.dump(data, write_file, indent=2)

    def tearDown(self):
        os.remove(self.FILE_PATH)


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
