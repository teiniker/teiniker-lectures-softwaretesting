import re


class ValidationError(Exception):
    pass


def operation(value):
    print('operation({})'.format(value))
    if value < 1 or value > 99:
        raise ValidationError('Invalid data value!')
    return value

