# Exercise: Coditional Statements, Loops, Functions 
#
# Implement the function "fibonacci_numbers()" which calculates the fibonacci 
# sequence with a given size (number of elements).
# Note that:
#     x[0] = 0
#     x[1] = 1
#     x[n] = x[n-1] + x[n-2]
 
def fibonacci_numbers(size):
    """Calculate the Fibonacci sequence of a given size."""
    pass


# Verify implementation

assert [] == fibonacci_numbers(0)
assert [0] == fibonacci_numbers(1)
assert [0, 1] == fibonacci_numbers(2)
assert [0, 1, 1] == fibonacci_numbers(3)
assert [0, 1, 1, 2, 3, 5, 8] == fibonacci_numbers(7)
assert [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377] == fibonacci_numbers(15)