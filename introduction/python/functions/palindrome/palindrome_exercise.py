# Exercise: Conditional Statements, Loops, Functions
#
# Implement a funcation called "is_palindrome()" which checks if a given 
# string is a palindrome (True) or not (False).
#
# Note that: A palindrome is a sequence of characters which reads the same 
# backward as forward. 

def is_palindrome(str):
    """Check if the given string is a palindrome."""     
    pass 


# Verify implementation

assert is_palindrome('00')  
assert not is_palindrome('011')
assert is_palindrome('000010000')

assert is_palindrome('otto')
assert is_palindrome('amanaplanacanalpanama') # A man, a plan, a canal - Panama 
