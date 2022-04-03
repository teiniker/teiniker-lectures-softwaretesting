import unittest
from order import Order, OrderLine, Product

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

    # Custom creation methods

    def createOrder(self):
        order = Order(7)
        order.lines.append(OrderLine(Product('dvd', 1799), 3))
        order.lines.append(OrderLine(Product('cd', 1299), 2))
        return order

if __name__ == '__main__':
    unittest.main()