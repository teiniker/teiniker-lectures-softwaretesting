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

    # Custom assert methods

    def assertEqualProduct(self,expected,actual):
        self.assertEqual(expected.description, actual.description, 'different Product.description')
        self.assertEqual(expected.price, actual.price, 'different Product.price')

    def assertEqualOrderLine(self, expected, actual, msg=''):
        self.assertEqual(expected.quantity, actual.quantity, 'different OrderLine.quantity'+msg)
        self.assertEqualProduct(expected.product, actual.product)

    def assertEqualsOrder(self, expected, actual):
        self.assertEqual(expected.id, actual.id)
        self.assertEqual(len(expected.lines), len(actual.lines))
        length = len(expected.lines)
        for i in range(length):
            self.assertEqualOrderLine(expected.lines[i], actual.lines[i], ' in line: ' + str(i))

    # Custom creation methods

    def createOrder(self):
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))
        return order

if __name__ == '__main__':
    unittest.main()