import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SchedulePage:
    pass 
    # TODO

class LoginPage:
    pass
    # TODO
    

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testLookup(self):
        login_page = LoginPage(self.driver)
        login_page.username = 'stm'
        login_page.password = 'stm'
        schedule_page = login_page.login()

        lecture = schedule_page.get_lecture()
        schedule_page.logout()
        
        self.assertEqual('09:00-10:30\nLE - SW Testing - X/ONL/Teams\nTeiniker', lecture)


if __name__ == '__main__':
    unittest.main()
