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

    def testDelegationFixture(self):

        # Setup
        order = self.createOrder()

        # Exercise

        # Verify
        self.assertEqual(7, order.id)
        self.assertEqual(3, order.lines[0].quantity)
        self.assertEqual('dvd', order.lines[0].product.description)
        self.assertEqual(1799, order.lines[0].product.price)
        self.assertEqual(2, order.lines[1].quantity)
        self.assertEqual('cd', order.lines[1].product.description)
        self.assertEqual(1299, order.lines[1].product.price)

    # TODO: create a custom creation method


if __name__ == '__main__':
    unittest.main()