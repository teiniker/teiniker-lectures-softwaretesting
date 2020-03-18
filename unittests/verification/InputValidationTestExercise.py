import unittest

# Custom exception defintion
class ValidationError(Exception):
   pass     # pass is a nul operation (placeholder)

# System Under Test
class User:
    def __init__(self, id, username, password):
        if not isinstance(id, int):
                raise TypeError('Invalid id: wrong type!');
        if id < 0:
            raise ValueError('Invalid id: should be a positive number!')
        if len(username) < 5:
            raise ValueError('Invalid username: too short!')
        if len(password) < 12:
            raise ValidationError('Invalid password: too short!')

        self.id = id
        self.username = username
        self.password = password


# TODO: Implement test cases for a code coverage of 100%

# Example:
#   def testAssertIdValue(self):
#        with self.assertRaises(ValueError):
#            user = User(-7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

# $ coverage3 run -m unittest unittests/verification/InputValidationTestExercise.py
# $ coverage3 report -m
# $ coverage3 html

