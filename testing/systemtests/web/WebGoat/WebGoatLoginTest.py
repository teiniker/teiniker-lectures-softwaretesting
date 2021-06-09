import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testLoginLogout(self):
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:8080/WebGoat/login")
        self.driver.find_element(By.ID, "exampleInputEmail1").send_keys("student")
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys("student")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()

        #...
        time.sleep(1)

        self.driver.get("http://localhost:8080/WebGoat/logout")

if __name__ == '__main__':
    unittest.main()
