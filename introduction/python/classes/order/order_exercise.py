# Exercise: Classes, Associations, Inheritance
#
# Implement a base class called "Entity" together with the following
# Subclasses:
#   [Order] ---[*]-> [OrderLine] ---[1]-> [Product]
#
# Entity: 
#   Attribute: id
#   Methods: __init__(), __eq__()
#
# Product:
#   Attributes: description, price
#   Methods: __init__(), __str__()
# 
# OrderLine:
#   Attributes: quantity, product
#   Methods: __init__(), __str__()
# 
# Order:
#   Attributes: name
#   Methods: __init__(), add_line(), __str__()  

class Entity():
    pass

class Product(Entity):
    pass

class OrderLine(Entity):
    pass

class Order(Entity):
    pass


# Verify implementations

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
