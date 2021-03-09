
class Resistor():
    """Simulates a resistor with a given tolerance."""

    def __init__(self, value, tolerance=2):
        self._value = value              
        self._tolerance = tolerance       
        # self.tolerance = 2

    def get_value(self):
        return self._value

    def get_tolerance(self):
        return self._tolerance

    def serial(self, resistor):
        self._value += resistor.get_value()

    def parallel(self, resistor):
        r1 = self._value
        r2 = resistor.get_value()
        self._value = r1 * r2 / float(r1 + r2)
         

# Verify implementation

r1 = Resistor(1000)
assert 1000 == r1.get_value()
assert 2 == r1.get_tolerance()

r2 = Resistor(470,5)
assert 470 == r2.get_value()
assert 5 == r2.get_tolerance()

r1.serial(r2)
assert 1000+470 == r1.get_value()

r1 = Resistor(1200)
r2 = Resistor(150)
r1.parallel(r2)
expected = 1200*150 / float(1200+150)
assert abs(expected - r1.get_value()) <= 1E-6