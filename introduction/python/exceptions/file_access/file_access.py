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
            raise DataAccessError(f'File not found: {self.filename}') 


# Verify Implementation

dao = DataAccessObject('data.csv')
values = dao.readData()
print(values)

try:
    dao = DataAccessObject('datx.csv')
    values = dao.readData()
    print(values)
except DataAccessError as e:
    print(e)    