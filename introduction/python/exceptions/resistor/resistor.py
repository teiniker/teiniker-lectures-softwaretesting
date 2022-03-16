
class Resistor():
    """Model of a resistor with a given tolerance."""

    def __init__(self, value, tolerance=2):
        if value < 0:
            raise ValueError('Invalid value!')
        if tolerance < 0:
            raise ValueError('Invalid tolerance!')

        self.__value = value              
        self.__tolerance = tolerance       

    def __repr__(self):
        return 'Resistor({}, {})'.format(self.__value, self.__tolerance)

    def __str__(self):
        return 'Resistor: value={}, tolerance={}'.format(self.__value, self.__tolerance)    

    def __eq__(self, other):
        if self.__value == other.__value and self.__tolerance == other.__tolerance:
            return True
        else:
            return False

    def __add__(self, other):
        return Resistor(self.__value + other.__value)


# Verify implementation

try:
    r1 = Resistor(1000)
    #...
except ValueError as e: 
    print("Resistor object can't be created: {}".format(e))    
else:    
    print("No exception thrown.")


try:
    r1 = Resistor(-1000)
    #...
except ValueError as e: 
    print("Resistor object can't be created: {}".format(e))    
finally:    
    print("Do some clean-up.")    