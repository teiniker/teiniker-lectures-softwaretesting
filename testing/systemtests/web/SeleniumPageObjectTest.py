import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://stundenplan.fh-joanneum.at/')

    def username(self, username):
        self.username = username

    def password(self, password):
        self.password = password

    def login(self):
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(self.username)
        self.driver.find_element(By.NAME, "pass").send_keys(self.password)
        self.driver.find_element(By.NAME, "login").click()
        return LogoutPage(self.driver)


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testLoginLogout(self):
        login_page = LoginPage(self.driver)
        login_page.username('swd')
        login_page.password('swd')
        logout_page = login_page.login()
        # ...
        logout_page.logout();


if __name__ == '__main__':
    unittest.main()