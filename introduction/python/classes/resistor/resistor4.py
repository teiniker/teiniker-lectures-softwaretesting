
class Resistor():
    def __init__(self, value, tolerance):
        self.value = value              
        self.tolerance = tolerance       

    @property
    def value(self):
        print(f'get value: {self._value}')
        return self._value

    @value.setter
    def value(self, value):
        print(f'set value: {value}')
        self._value = value

    @property
    def tolerance(self):
        print(f'get tolerance: {self._tolerance}')
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        print(f'set tolerance: {tolerance}')
        self._tolerance = tolerance


    def __add__(self, other): # +
        value = self._value + other._value
        tolerance = self._max(self.tolerance, other.tolerance)
        return Resistor(value, tolerance)

    def _max(self, a, b):
        if(a > b):
            return a
        else:
            return b


# Verify implementation

r1 = Resistor(100,1)
assert 100 == r1.value
assert 1 == r1.tolerance

r2 = Resistor(330,5)
r2.value = 470
assert 470 == r2.value
assert 5 == r2.tolerance

r = r1 + r2
assert 100+470 == r.value
assert 5 == r.tolerance