import unittest
from user import User, Mail

class UserTest(unittest.TestCase):

    def testInlineFixture(self):
        # setup
        mail = Mail('homer.simpson@springfield.com')
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)

        # exercise

        # verify
        self.assertEqual(7, user.id)
        self.assertEqual('homer', user.username)
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', user.password)
        self.assertEqual('homer.simpson@springfield.com', user.mail.adress)


    # Implicit fixture setup
    def setUp(self):
        mail = Mail('homer.simpson@springfield.com')
        self.user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)

    def testImplicitFixture(self):
        # exercise

        # verify
        self.assertEqual(7, self.user.id)
        self.assertEqual('homer', self.user.username)
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', self.user.password)
        self.assertEqual('homer.simpson@springfield.com', self.user.mail.adress)


    def testDelegationFixture(self):
        # setup
        user = self.createUser()

        # exercise

        # verify
        self.assertEqual(7, user.id)
        self.assertEqual('homer', user.username)
        self.assertEqual('Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', user.password)
        self.assertEqual('homer.simpson@springfield.com', user.mail.adress)


    def testModifiedDelegationFixture(self):
        # setup
        user = self.createUser() # default values
        user.password = 'SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L='

        # exercise

        # verify
        self.assertEqual(7, user.id)
        self.assertEqual('homer', user.username)
        self.assertEqual('SBiFOHaODQY65DJBS8vxsoihdknrtdKqq3lbODaQT4L=', user.password)
        self.assertEqual('homer.simpson@springfield.com', user.mail.adress)


    # Creation methods

    def createUser(self):
        mail = Mail('homer.simpson@springfield.com')
        user = User(7, 'homer', 'Kqq3lbODaQT4LvxsoihdknrtdSBiFOHaODQY65DJBS8=', mail)
        return user

if __name__ == '__main__':
    unittest.main()