import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testLoginLogout(self):
        self.driver.get('http://stundenplan.fh-joanneum.at/')
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys('swd')
        self.driver.find_element(By.NAME, "pass").send_keys('swd')
        self.driver.find_element(By.NAME, "login").click()
        # ...
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


if __name__ == '__main__':
    unittest.main()
