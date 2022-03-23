
class Resistor():
    """Model of a resistor with a given tolerance."""

    def __init__(self, value, tolerance=2):
        self.__value = value              
        self.__tolerance = tolerance  
    
    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value 

    def get_tolerance(self):
        return self.__tolerance

    def set_tolerance(self, tolerance):
        self.__tolerance = tolerance
    
    
    def __repr__(self):
        return f'Resistor({self.__value}, {self.__tolerance})'

    def __str__(self):
        return f'Resistor: value={self.__value}, tolerance={self.__tolerance}'


    def __eq__(self, other):
        if self.__value == other.__value and self.__tolerance == other.__tolerance:
            return True
        else:
            return False

    def __add__(self, other): # +
        value = self.__value + other.__value
        tolerance = self.__max(self.__tolerance, other.__tolerance)
        return Resistor(value, tolerance)

    def __max(self, a, b):
        if(a > b):
            return a
        else:
            return b


# Verify implementation

r1 = Resistor(1000)
assert 1000 == r1.get_value()
assert 2 == r1.get_tolerance()

r2 = Resistor(470,5)
assert 470 == r2.get_value()
assert 5 == r2.get_tolerance()

r = Resistor(330, 2)
assert 'Resistor(330, 2)' == repr(r)

r = Resistor(330, 2)
assert 'Resistor: value=330, tolerance=2' == str(r)

r = r1 + r2
assert 1000+470 == r.get_value()

r1 = Resistor(2700,2)
r2 = Resistor(2700,2)
assert r1 is r1
assert r1 == r2
