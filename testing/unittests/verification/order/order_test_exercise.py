import unittest

from order import Order, OrderLine, Product

# Exercise: Result Verification / Custom Asserts - Order
#
# Implement the following custom assert methods
#   assertEqualProduct()
#   assertEqualOrderLine()
#   assertEqualsOrder()
# which can be used to compare two Order object trees attribute by 
# attribute.

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