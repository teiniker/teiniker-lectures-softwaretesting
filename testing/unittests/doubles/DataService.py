import unittest
from unittest.mock import Mock

# System Under Test

class ServiceError(Exception):
    pass


class DataAccessError(Exception):
    pass


class DataService:
    def __init__(self, dao):
        self.dao = dao

    def csvData(self):
        try:
            values = self.dao.readData()
            csv = ','.join(str(value) for value in values)
            return csv
        except DataAccessError:
            raise ServiceError('Can not read data!')


# Test cases
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


    def testDataAccessError(self):
        with self.assertRaises(ServiceError):
            # Setup
            self.dao = Mock()  # Mock() replaces DataAccessObject
            self.dao.readData.side_effect = DataAccessError('Can not read data!')
            self.service = DataService(self.dao)
            # Exercise
            self.service.csvData()

# $ coverage3 run -m unittest unittests/doubles/DataService.py
# $ coverage3 report -m
# $ coverage3 html
# Browser: file:///home/student/github/teiniker-lectures-softwaretesting/htmlcov/index.html

