import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def testLookup(self):
        self.driver.get("http://stundenplan.fh-joanneum.at/")
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys("ste")
        self.driver.find_element(By.NAME, "pass").send_keys("ste")
        self.driver.find_element(By.NAME, "login").click()
        assert self.driver.find_element(By.CSS_SELECTOR,".event:nth-child(116)").text == "08:00-09:30\nVO - SWT - G.AP147.119\nTeiniker"

        self.driver.find_element(By.LINK_TEXT, "Logout").click()


if __name__ == '__main__':
    unittest.main()
