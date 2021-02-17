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


# Test cases
class UserTest(unittest.TestCase):

    def testAssertEachProperty(self):
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

        # Verification
        self.assertEqual(7, user.id, 'different id')
        self.assertEqual('homer', user.username, 'different username')
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', user.password, 'different password')

    def testAssertIdType(self):
        with self.assertRaises(TypeError):
            user = User('7', 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    def testAssertIdValue(self):
        with self.assertRaises(ValueError):
            user = User(-7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    def testAssertUsername(self):
        with self.assertRaises(ValueError):
            user = User(7, 'ho', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

    def testAssertPassword(self):
        with self.assertRaises(ValidationError):
            user = User(7, 'homer', 'Kqq3')

if __name__ == '__main__':
    unittest.main()