import unittest

class Product:
    def __init__(self, description, price):
        self.description = description
        self.price = price


class ProductTest(unittest.TestCase):

    def testProduct(self):
        product = Product('dvd', 1799)
        expected = Product('dvd', 1799)
        self.assertEqualProduct(expected, product)

    # Custom assert method

    def assertEqualProduct(self,expected,actual):
        self.assertEqual(expected.description, actual.description, 'different description')
        self.assertEqual(expected.price, actual.price, 'different price')


if __name__ == '__main__':
    unittest.main()