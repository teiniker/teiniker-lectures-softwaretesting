class Product:
    def __init__(self, description, price):
        if len(description) == 0:
            raise ValueError('Invalid description: "{}"!'.format(description))
        if price < 0:
            raise ValueError('Invalid price: {}!'.format(price))
        
        self.description = description
        self.price = price
