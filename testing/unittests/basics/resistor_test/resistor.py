
class Resistor():
    """Model of a resistor with a given tolerance."""
    
    vendor = 'Neuhold Electronics'

    def __init__(self, value, tolerance=2):
        self.value = value              
        self.tolerance = tolerance       

    def __repr__(self):
        return 'Resistor({}, {})'.format(self.value, self.tolerance)

    def __str__(self):
        return 'Resistor: value={}, tolerance={}'.format(self.value, self.tolerance)    

    def __eq__(self, other):
        if self.value == other.value and self.tolerance == other.tolerance:
            return True
        else:
            return False

    def __add__(self, other):
        return Resistor(self.value + other.value)


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

r = r1 + r2
assert 1000+470 == r.value

r1 = Resistor(2700,2)
r2 = Resistor(2700,2)
assert r1 is r1
assert r1 == r2