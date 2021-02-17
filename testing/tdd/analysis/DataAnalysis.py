import csv
import statistics


class DataAccessError(Exception):
    pass


class ServiceError(Exception):
    pass


class DataAccessObject:
    def __init__(self, filename):
        self.filename = filename

    def readData(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                data = list(reader)
            values = []
            for value in data:
                values.append(float(value[1]))
            return values
        except FileNotFoundError:
            raise DataAccessError('File not found: ' + self.filename)


class DataAnalysisService:
    def __init__(self, dao):
        self.dao = dao

    def meanValue(self):
        try:
            values = self.dao.readData()
            return statistics.mean(values)
        except DataAccessError:
            raise ServiceError('Can not read data!')

    def maxValue(self):
        try:
            values = self.dao.readData()
            values.sort()
            return values[-1]
        except DataAccessError:
            raise ServiceError('Can not read data!')
