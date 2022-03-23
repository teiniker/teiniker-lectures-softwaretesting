class Entity():
    """Base class for entity classed which provide an id."""
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id


class Product(Entity):
    """Product class which supports a description and a price."""
    def __init__(self, id, description, price):
        super().__init__(id)
        self.description = description
        self.price = price

    def __str__(self):
        return f'Product: id={self.id}, description="{self.description}", price={self.price}'            


class OrderLine(Entity):
    def __init__(self, id, quantity, product):
        super().__init__(id)
        self.quantity = quantity
        self.product = product

    def __str__(self):
        return f'OrderLine: id={self.id}, quantity={self.quantity}, product={self.product}'           


class Order(Entity):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)    

    def __str__(self):    
        lines_str = '; '.join([str(elem) for elem in self.lines])
        return f'Order: id={self.id}, name={self.name}, lines=[{lines_str}]'


e1 = Entity(7)
p1 = Product(3, "Pizza Frutti di Mare", 8.80)
p2 = Product(3, "Pizza Frutti di Mare", 8.80)
assert p1 == p2

order = Order(1, "Pizza Order")
line1 = OrderLine(2, 1, Product(3, "Pizza Frutti di Mare", 8.80))
line2 = OrderLine(4, 1, Product(5, "Pizza Quattro Formaggi", 8.20))
order.add_line(line1)
order.add_line(line2)
print(order)

assert 1 == order.id
assert "Pizza Order" == order.name 

assert 2 == order.lines[0].id
assert 4 == order.lines[1].id

assert 3 == order.lines[0].product.id 
assert 5 == order.lines[1].product.id 
