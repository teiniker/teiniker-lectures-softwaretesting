import unittest
import os
import json

class JsonFileTest(unittest.TestCase):
    FILE_PATH = 'data_file.json'

    def setUp(self):
        data = {'person': {'name': 'John', 'age': 30, 'city': "New York"}}
        with open(self.FILE_PATH, "w") as write_file:
            json.dump(data, write_file, indent=2)

    def tearDown(self):
        os.remove(self.FILE_PATH)

    def testDeserializationFromFile(self):
        # Exercise
        with open(self.FILE_PATH, "r") as read_file:
            data = json.load(read_file)
        # Verify
        expected = {'person': {'name': 'John', 'age': 30, 'city': 'New York'}}
        self.assertDictEqual(expected, data)

    def testModifyJsonFile(self):
        # Setup
        data = {'person': {'name': 'John', 'age': 30, 'city': "New York"}}
        # Exercise
        data['person']['age'] = 50
        with open(self.FILE_PATH, "w") as write_file:
            json.dump(data, write_file, indent=2)
        # Verify
        with open(self.FILE_PATH, "r") as read_file:
            data = json.load(read_file)
        expected = {'person': {'name': 'John', 'age': 50, 'city': 'New York'}}
        self.assertDictEqual(expected, data)

    def testSerializationToString(self):
        # Setup
        data = { "person": {"name":"John", "age":30, "city":"New York"}}
        # Exercise
        json_string = json.dumps(data)
        # Verify
        self.assertEqual('{"person": {"name": "John", "age": 30, "city": "New York"}}', json_string)


    def testDeserializationFromString(self):
        # Setup
        json_string = '{"person": {"name": "John", "age": 30, "city": "New York"}}'
        # Exercise
        data = json.loads(json_string)
        # Verify
        expected = {'person': {'name': 'John', 'age': 30, 'city': 'New York'}}
        self.assertEqual(expected, data)

if __name__ == '__main__':
    unittest.main()

# References:
# https://docs.python.org/3/library/json.html#module-json
# https://realpython.com/python-json/
