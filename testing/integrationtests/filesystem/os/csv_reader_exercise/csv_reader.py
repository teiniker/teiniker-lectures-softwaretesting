import csv
import statistics


class DataAccessError(Exception):
    pass

class Order:
    def __init__(self, id, part, quantity):
        self.id = id
        self.part = part
        self.quantity = quantity
     
    def __str__(self):
        return 'Order: id={}, part={}, quantity={}'.format(self.id, self.part, self.quantity)    


class CsvDataReader:
    def read_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                orders = []
                for row in reader:    
                    print('id: {} part:{} quantity:{}'.format(row[0],row[1],row[2]))
                    orders.append(Order(int(row[0]), row[1], row[2]))
                return orders        
        except FileNotFoundError:
            raise DataAccessError('File not found: ' + filename)
    
    def save_csv(self, filename, orders):
        with open(filename, 'w') as file:
            csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            for o in orders:
                csv_writer.writerow([o.id, o.part, o.quantity])


