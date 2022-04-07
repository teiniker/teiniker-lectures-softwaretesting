import unittest

from order import Order, OrderLine, Product

class OrderTest(unittest.TestCase):

    def test_order(self):
        # Setup
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))

        # Verify
        expected = self.create_order()
        self.assert_equals_order(expected, order)

    # Custom assert methods

    def assert_equal_product(self,expected,actual):
        self.assertEqual(expected.description, actual.description, 'different Product.description')
        self.assertEqual(expected.price, actual.price, 'different Product.price')

    def assert_equal_order_line(self, expected, actual, msg=''):
        self.assertEqual(expected.quantity, actual.quantity, 'different OrderLine.quantity'+msg)
        self.assert_equal_product(expected.product, actual.product)

    def assert_equals_order(self, expected, actual):
        self.assertEqual(expected.id, actual.id)
        self.assertEqual(len(expected.lines), len(actual.lines))
        length = len(expected.lines)
        for i in range(length):
            self.assert_equal_order_line(expected.lines[i], actual.lines[i], ' in line: ' + str(i))

    # Custom creation methods

    def create_order(self):
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))
        return order

if __name__ == '__main__':
    unittest.main()
