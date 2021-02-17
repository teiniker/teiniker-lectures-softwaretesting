# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.
# Within a module, the module’s name (as a string) is available
# as the value of the global variable __name__.

# “Private” instance variables that cannot be accessed except from inside
# an object don’t exist in Python.
# There is a convention that is followed by most Python code: a name prefixed
# with an underscore (e.g. _spam) should be treated as a non-public part of
# the API (whether it is a function, a method or a data member).

class Resistor():
    vendor = 'Conrad'   # class variable

    # It makes sense to specify an initial default value in the body of the
    # __init__() method; if you do this for an attribute, you don’t have to
    # include a parameter for that attribute.

    def __init__(self, value):
        self.value = value          # instance variable
        self.tolerance = 2          # instance variable (default value)

    def getValue(self):
        return self.value

    def getTolerance(self):
        return self.tolerance

    def add(self, resistor):
        # TODO check tolerance
        self.value += resistor.getValue()

