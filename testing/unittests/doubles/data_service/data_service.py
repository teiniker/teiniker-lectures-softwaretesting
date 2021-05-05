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


