import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:8080/WebGoat/login")

    def username(self, username):
        self.username = username

    def password(self, password):
        self.password = password

    def login(self):
        self.driver.find_element(By.ID, "exampleInputEmail1").send_keys("student")
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("student")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        return MainPage(self.driver)


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.get("http://localhost:8080/WebGoat/logout")


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testLoginLogout(self):
        login_page = LoginPage(self.driver)
        login_page.username('student')
        login_page.password('student')
        main_page = login_page.login()
        #...
        time.sleep(5) # just to show that we are logged in
        main_page.logout()


if __name__ == '__main__':
    unittest.main()
