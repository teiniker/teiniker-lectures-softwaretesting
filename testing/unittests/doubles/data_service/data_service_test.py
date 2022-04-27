import unittest
from unittest.mock import Mock
from data_service import DataService, DataAccessError, ServiceError

class DataServiceTest(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.dao = None
        self.service = None

    def test_csv_data(self):
        # Setup
        self.dao = Mock()  # Mock() replaces DataAccessObject
        self.dao.read_data.return_value = [0.8273, 0.7822, 0.9731, 0.1239, 0.9898]
        self.service = DataService(self.dao)

        # Exercise
        values = self.service.csv_data()

        # State verification
        expected = "0.8273,0.7822,0.9731,0.1239,0.9898"
        self.assertEqual(expected, values)
        # Behavioral verification
        self.dao.read_data.assert_called_once()
        self.assertEqual(1, self.dao.read_data.call_count)

    def test_data_access_error(self):
        # Setup
        self.dao = Mock()  # Mock() replaces DataAccessObject
        self.dao.read_data.side_effect = DataAccessError('Can not read data!')
        self.service = DataService(self.dao)
        # Exercise
        with self.assertRaises(ServiceError):
            self.service.csv_data()

if __name__ == '__main__':
    unittest.main()
