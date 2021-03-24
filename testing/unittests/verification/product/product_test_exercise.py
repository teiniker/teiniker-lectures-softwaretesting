import unittest

from product import Product

# Exercise: Result Verification / Custom Asserts - Product
#
# Implement a custom assert method called "assertEqualProduct()"
# which can be used to compare two Product objects attribute by 
# attribute.

class ProductTest(unittest.TestCase):

    def testProduct(self):
        product = Product('dvd', 1799)
        expected = Product('dvd', 1799)
        self.assertEqualProduct(expected, product)


if __name__ == '__main__':
    unittest.main()