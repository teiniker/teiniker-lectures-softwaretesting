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
        self.id = id
        self.lines = []
        