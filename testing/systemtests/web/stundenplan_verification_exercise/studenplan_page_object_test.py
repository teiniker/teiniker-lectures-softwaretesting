import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Exercise: Page Object Pattern - Stundenplan
#
# Implement the following Page Object classes to make the StundenplanTest run:
#    LoginPage
#       def __init__(self, driver):
#       def username(self, username):
#       def password(self, password):
#       def login(self):
#    SchedulePage
#       def __init__(self, driver):
#       def get_lectures(self):
#           read the lectures from the table and put the text into a list of strings.
#       def logout(self):

class StundenplanTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testLookup(self):
        login_page = LoginPage(self.driver)
        login_page.username('ste')
        login_page.password('ste')
        schedule_page = login_page.login()
        lectures = schedule_page.get_lectures()
        schedule_page.logout()
        self.assertEqual("08:00-09:30\nVO - SWT - G.AP147.119\nTeiniker", lectures[0])



if __name__ == '__main__':
    unittest.main()
