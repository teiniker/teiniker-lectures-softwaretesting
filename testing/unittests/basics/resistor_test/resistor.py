
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
