import unittest

from product import Product

class ProductTest(unittest.TestCase):

    def testProduct(self):
        product = Product('dvd', 1799)
        self.assertEqual('dvd', product.description)
        self.assertEqual(1799, product.price)

    def testProduct_InvalidPrice(self):
        with self.assertRaises(ValueError):
            Product('dvd', -1790)

    def testProduct_InvalidDescription(self):
        with self.assertRaises(ValueError):
            Product('', 1799)

if __name__ == '__main__':
    unittest.main()