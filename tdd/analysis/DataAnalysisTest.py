import unittest
from tdd.analysis.DataAnalysis import *


class AnalysisServiceTest(unittest.TestCase):

    def setUp(self):
        self.dao = DataAccessObject('tdd/analysis/data.csv')
        self.service = DataAnalysisService(self.dao)

    def testReadData(self):
        # Exercise
        values = self.dao.readData()
        # Verify
        expected = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        self.assertEqual(expected, values)

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

    def testReadData_FileNotFound(self):
        with self.assertRaises(DataAccessError):
            # Setup
            dao = DataAccessObject('vales.csv')
            dao.readData()

    def testMeanValue_FileNotFound(self):
        with self.assertRaises(ServiceError):
            # Setup
            dao = DataAccessObject('vales.csv')
            service = DataAnalysisService(dao)
            service.meanValue()

    def testMaxValue_FileNotFound(self):
        with self.assertRaises(ServiceError):
            # Setup
            dao = DataAccessObject('vales.csv')
            service = DataAnalysisService(dao)
            service.maxValue()
