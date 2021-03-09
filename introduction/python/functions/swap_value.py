# Multiple return values of a function

def swap_value(a,b):
    """Change the values of a and b"""
    return b, a

a = 7
b = 11
a,b = swap_value(a,b)
assert a == 11
assert b == 7

