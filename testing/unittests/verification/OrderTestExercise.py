import unittest

class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price


class OrderLine:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Order:
    def __init__(self, id):
        self.id = id;
        self.lines = []


class OrderTest(unittest.TestCase):

    def testOrder(self):
        # Setup
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))

        # Verify
        expected = self.createOrder()
        self.assertEqualsOrder(expected, order)

    # TODO: create the custom assert methods


    # Custom creation methods

    def createOrder(self):
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))
        return order

if __name__ == '__main__':
    unittest.main()