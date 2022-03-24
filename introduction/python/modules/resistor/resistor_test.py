from resistor import Resistor

# Verify implementation

try:
    r1 = Resistor(1000, -1)
    #...
except ValueError as e: 
    print("Resistor object can't be created: {}".format(e))    
else:    
    print("No exception thrown.")


try:
    r1 = Resistor(-1000, 2)
    #...
except ValueError as e: 
    print("Resistor object can't be created: {}".format(e))    
finally:    
    print("Do some clean-up.")    