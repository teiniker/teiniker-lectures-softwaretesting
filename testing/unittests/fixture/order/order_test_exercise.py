import unittest
from order import Order, OrderLine, Product

# Exercise: Fixture Setup - Order 
# 
# Implement a custom creation method called "createOrder()" which 
# sets up the [Order] --[*]-> [OrderLine] --[1]-> [Product] objects
# used in the given test case.  

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



if __name__ == '__main__':
    unittest.main()