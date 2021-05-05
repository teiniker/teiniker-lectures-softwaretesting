import unittest
from unittest.mock import Mock


class MockTest(unittest.TestCase):

    def setUp(self):
        self.json = Mock()  # Mock() replaces any object

    def testCalled(self):
        # exercise
        self.json.loads('{"key": "value"}')

        # verify
        self.json.loads.assert_called()
        self.json.loads.assert_called_once()
        self.json.loads.assert_called_with('{"key": "value"}')
        self.json.loads.assert_called_once_with('{"key": "value"}')


    def testCalledOnce(self):
        # exercise
        self.json.loads('{"key": "value"}')
        self.json.loads('{"key": "value"}')

        # verify
        with self.assertRaises(AssertionError): # loads() is called twice
            self.json.loads.assert_called_once()


    def testCalledCount(self):
        # exercise
        self.json.loads('{"key": "value"}')
        self.json.loads('{"key": "value"}')

        # verify
        self.assertEqual(2, self.json.loads.call_count)


    # When writing tests, it is important to ensure that the results 
    # are predictable.
    # You can use Mock to eliminate uncertainty from your code 
    # during testing.

    def testReturnValue(self):
        # setup
        self.json.random.return_value = 666

        # exercise
        randomValue = self.json.random()

        # verify
        self.assertEqual(666, randomValue)
