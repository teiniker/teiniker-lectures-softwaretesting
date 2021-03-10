
class Resistor():
    """Model of a resistor with a given tolerance."""

    def __init__(self, value, tolerance=2):
        self._value = value              
        self._tolerance = tolerance       

    def get_value(self):
        return self._value

    def get_tolerance(self):
        return self._tolerance

    def __repr__(self):
        return 'Resistor({}, {})'.format(self.get_value(), self.get_tolerance())

    def __str__(self):
        return 'Resistor: value={}, tolerance={}'.format(self.get_value(), self.get_tolerance())    

    def __eq__(self, other):
        if self._value == other._value and self._tolerance == other._tolerance:
            return True
        else:
            return False

    def __add__(self, other):
        return Resistor(self._value + other._value)


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