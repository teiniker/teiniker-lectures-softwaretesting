
class Resistor():
    """Class using private attributes together with getter and setter methods."""
    def __init__(self, value, tolerance):
        self.__value = value              
        self.__tolerance = tolerance       

    def get_value(self):
        return self.__value

    def set_value(self, value):
        # Input validation
        self.__value = value 

    def get_tolerance(self):
        return self.__tolerance

    def set_tolerance(self, tolerance):
        self.__tolerance = tolerance

    def add(self, other):
        value = self.__value + other.__value
        tolerance = self.__max(self.__tolerance, other.__tolerance)
        return Resistor(value, tolerance)

    def __max(self, a, b):
        if(a > b):
            return a
        else:
            return b

# Verify implementation

r1 = Resistor(100,1)
assert 100 == r1.get_value()
assert 1 == r1.get_tolerance()

r2 = Resistor(330,5)
assert 330 == r2.get_value()
assert 5 == r2.get_tolerance()

r = r1.add(r2)
assert 100+330 == r.get_value()
assert 5 == r.get_tolerance()