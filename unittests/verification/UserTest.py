import unittest

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class UserTest(unittest.TestCase):

    def testAssertEachProperty(self):
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

        # Verification
        expected = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')
        self.assertEqual(expected.id, user.id, 'different id')
        self.assertEqual(expected.username, user.username, 'different username')
        self.assertEqual(expected.password, user.password, 'different password')


    def testCustomAssert(self):
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')

        # Verification
        expected = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=')
        self.assertEqualUser(expected, user)


    # Custom assert method

    def assertEqualUser(self,expected,actual):
        self.assertEqual(expected.id, actual.id, 'different id')
        self.assertEqual(expected.username, actual.username, 'different username')
        self.assertEqual(expected.password, actual.password, 'different password')

if __name__ == '__main__':
    unittest.main()