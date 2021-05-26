import unittest
from unittest.mock import Mock

from data_analysis import DataAnalysisService, DataAccessError, ServiceError


class AnalysisServiceTest(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()                               # DOC
        self.dao.readData.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        self.service = DataAnalysisService(self.dao)    # SUT


    def testMeanValue(self):
        # Exercise
        mean = self.service.meanValue()
        # Verify
        expected = (0.8273 + 0.7822 + 0.9731 + 0.1239 + 0.9898) / 5.0
        self.assertEqual(expected, mean, 1E-3)

    def testMaxValue(self):
        # Exercise
        min = self.service.maxValue()
        # Verify
        self.assertEqual(0.9898, min, 1E-3)

    def testMeanValue_FileNotFound(self):
        # Setup
        self.dao.readData.side_effect = DataAccessError()
        # Exercise
        with self.assertRaises(ServiceError):
            self.service.meanValue()

    def testMaxValue_FileNotFound(self):
       # Setup
        self.dao.readData.side_effect = DataAccessError()
        with self.assertRaises(ServiceError):
            self.service.maxValue()

if __name__ == '__main__':
    unittest.main()