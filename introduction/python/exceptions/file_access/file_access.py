import csv

class DataAccessError(Exception):
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

# Verify Implementation

try:
    dao = DataAccessObject('datx.csv')
    values = dao.readData()
    print(values)
except DataAccessError as e:
    print(e)    