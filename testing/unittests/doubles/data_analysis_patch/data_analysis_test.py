import unittest
from unittest.mock import Mock, patch

from data_analysis import DataAccessObject, DataAnalysisService, DataAccessError, ServiceError


class AnalysisServiceTest(unittest.TestCase):

    def setUp(self):
        self.dao = DataAccessObject('data.csv')
        self.service = DataAnalysisService(self.dao)

    # The following tests use the real DataAccessObject class, reading data
    # froma file.
    
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


    # The following tests replace the invocation of DataAccessObject.readData()
    # with a mocked version returning pre-configured data and exceptions.

    def testMeanValueMocked(self):
        # Setup
        # patch('module.class.method')
        with patch('data_analysis.DataAccessObject.readData') as mock_readData:
            mock_readData.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]        
            # Exercise
            mean = self.service.meanValue()
            # Verify
            self.assertEqual((1.0 + 2.0 + 3.0 + 4.0 + 5.0)/5.0, mean, 1E-3)    

    def testMaxValueMocked(self):
        # Setup
        with patch('data_analysis.DataAccessObject.readData') as mock_readData:
            mock_readData.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]        
            # Exercise
            min = self.service.maxValue()
            # Verify
            self.assertEqual(5.0, min, 1E-3)

    def testMeanValue_FileNotFound(self):
        # Setup
        with patch('data_analysis.DataAccessObject.readData') as mock_readData:
            mock_readData.side_effect = DataAccessError()        
            # Exercise        
            with self.assertRaises(ServiceError):
                self.service.meanValue()

    def testMaxValue_FileNotFound(self):
        # Setup
        with patch('data_analysis.DataAccessObject.readData') as mock_readData:
            mock_readData.side_effect = DataAccessError()        
            # Exercise        
            with self.assertRaises(ServiceError):
                self.service.maxValue()


if __name__ == '__main__':
    unittest.main()