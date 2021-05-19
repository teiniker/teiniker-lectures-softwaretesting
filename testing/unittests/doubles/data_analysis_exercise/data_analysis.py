import csv
import statistics


class DataAccessError(Exception):
    pass

class ServiceError(Exception):
    pass


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
