import unittest
from unittest.mock import Mock
from data_service import DataService, DataAccessError, ServiceError

class DataServiceTest(unittest.TestCase):

    def testCsvData(self):
        # Setup
        self.dao = Mock()  # Mock() replaces DataAccessObject
        self.dao.readData.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        self.service = DataService(self.dao)

        # Exercise
        values = self.service.csvData()

        # State verification
        expected = "0.8273,0.7822,0.9731,0.1239,0.9898"
        self.assertEqual(expected, values)
        # Behavioral verification
        self.dao.readData.assert_called_once()
        self.assertEqual(1, self.dao.readData.call_count)    

    def testDataAccessError(self):
        with self.assertRaises(ServiceError):
            # Setup
            self.dao = Mock()  # Mock() replaces DataAccessObject
            self.dao.readData.side_effect = DataAccessError('Can not read data!')
            self.service = DataService(self.dao)
            # Exercise
            self.service.csvData()


    def testCsvData2(self):
        # Setup
        self.dao = Mock()  # Mock() replaces DataAccessObject
        self.dao.readData.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        self.service = DataService(self.dao)

        # Exercise
        values = self.service.csvData()

        # State verification
        expected = "0.8273,0.7822,0.9731,0.1239,0.9898"
        self.assertEqual(expected, values)
        # Behavioral verification
        self.dao.readData.assert_called_once()
        self.assertEqual(1, self.dao.readData.call_count)    

if __name__ == '__main__':
    unittest.main()


