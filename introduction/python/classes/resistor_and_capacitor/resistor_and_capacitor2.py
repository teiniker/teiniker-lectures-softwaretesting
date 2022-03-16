class Part():
    def __init__(self, value, tolerance):
        self.tolerance = tolerance       
        self.value= value   

class Resistor(Part):
    def __init__(self, value, tolerance=2):
        super().__init__(value, tolerance)              
            
    def __str__(self):
        return 'Resistor: value={}Ohm, tolerance={}'.format(self.value, self.tolerance)    


class Capacitor(Part):
    def __init__(self, value, tolerance=5):
        super().__init__(value, tolerance)              

    def __str__(self):
        return 'Capacitor: value={}uF, tolerance={}'.format(self.value, self.tolerance)    


# Verify implementations

r1 = Resistor(1000)
assert 1000 == r1.value
assert 2 == r1.tolerance

r2 = Resistor(470,5)
assert 470 == r2.value
assert 5 == r2.tolerance

r = Resistor(330, 2)
assert 'Resistor: value=330Ohm, tolerance=2' == str(r)


c1 = Capacitor(1)
assert 1 == c1.value
assert 5 == c1.tolerance

c2 = Capacitor(100, 10)
assert 100 == c2.value
assert 10 == c2.tolerance

assert 'Capacitor: value=1uF, tolerance=5' == str(c1)

#print(help(Resistor))
#print(help(Capacitor))

#print(isinstance(r1, Resistor))
#print(isinstance(r1, Part))
#print(isinstance(r1, Capacitor))

print(issubclass(Resistor, Part))
print(issubclass(Capacitor, Part))
print(issubclass(Resistor, Capacitor))