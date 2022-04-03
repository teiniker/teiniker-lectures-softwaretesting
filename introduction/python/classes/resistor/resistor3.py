
class Resistor():
    """Class using operator overloading and magic methods."""

    def __init__(self, value, tolerance=2):
        self.value = value              
        self.tolerance = tolerance      
    
    def __repr__(self):
        return f'Resistor({self.value}, {self.tolerance})'

    def __str__(self):
        return f'Resistor: value={self.value}, tolerance={self.tolerance}'

    def __eq__(self, other):
        if self.value == other.value and self.tolerance == other.tolerance:
            return True
        else:
            return False

    def __add__(self, other): # +
        value = self.value + other.value
        tolerance = self._max(self.tolerance, other.tolerance)
        return Resistor(value, tolerance)

    def _max(self, a, b):
        if(a > b):
            return a
        else:
            return b


# Verify implementation

r1 = Resistor(1000)
assert 1000 == r1.value
assert 2 == r1.tolerance

r2 = Resistor(470,5)
assert 470 == r2.value
assert 5 == r2.tolerance

r = Resistor(330, 2)
assert 'Resistor(330, 2)' == repr(r)

r = Resistor(330, 2)
assert 'Resistor: value=330, tolerance=2' == str(r)

r = r1 + r2 # __add__()
assert 1000+470 == r.value

r1 = Resistor(2700,2)
r2 = Resistor(2700,2)
assert r1 is r1
assert r1 == r2 # __eq__()
