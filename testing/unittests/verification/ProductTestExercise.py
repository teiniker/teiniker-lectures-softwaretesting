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

    # TODO: create a custom assert method


if __name__ == '__main__':
    unittest.main()