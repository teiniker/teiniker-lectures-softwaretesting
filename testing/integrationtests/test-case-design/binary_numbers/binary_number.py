import re


class ValidationError(Exception):
    pass


def operation(data):
    print(data)
    pattern = '^[01]{1,8}$'  # Regular expression
    result = re.match(pattern, data)
    if result:
        return int(data, 2)
    else:
        raise ValidationError('Invalid data value!')

# References:
# > Python RegEx
#   https://www.programiz.com/python-programming/regex
# > Regular Expression HOWTO
#   https://docs.python.org/3/howto/regex.html
