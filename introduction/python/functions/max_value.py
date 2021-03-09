# Using a docstring 

def max_value(a, b):
    """Calculate the maximum of two numbers"""
    if a > b:
        return a
    else:
        return b    

max = max_value(7,11)
assert 11 == max       
assert 'Calculate the maximum of two numbers' == max_value.__doc__

# help(max_value)
