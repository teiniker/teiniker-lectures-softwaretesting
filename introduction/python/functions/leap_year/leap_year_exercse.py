# Exercise: Conditional Statements, Functions
#
# Implement the function "is_leap_year()":
# Note that: year % 4   is     a leap year: e.g. 2020
#            year % 100 is not a leap year: e.g. 2100 
#            year % 400 is     a leap year: e.g. 2000

def is_leap_year(year):
    """Check if a given year is a leap year or not."""
    pass


# Verify implementation
assert is_leap_year(2000)
assert is_leap_year(2020)
assert not is_leap_year(2021)
assert not is_leap_year(2100)
