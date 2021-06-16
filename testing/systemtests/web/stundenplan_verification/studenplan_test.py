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
        self.driver.find_element(By.NAME, "user").send_keys("stm")
        self.driver.find_element(By.NAME, "pass").send_keys("stm")
        self.driver.find_element(By.NAME, "login").click()

        self.driver.find_element(By.NAME, "new_jg").click()
        dropdown = self.driver.find_element(By.NAME, "new_jg")
        dropdown.find_element(By.XPATH, "//option[. = '2020']").click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(1) > option:nth-child(2)").click()
        self.driver.find_element(By.NAME, "new_date").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(38)").click()
        self.driver.find_element(By.NAME, "new_values").click()       
        self.driver.find_element(By.CSS_SELECTOR, ".event:nth-child(117)").click()
        
        assert self.driver.find_element(By.CSS_SELECTOR, ".event:nth-child(117)").text == '09:00-10:30\nLE - SW Testing - X/ONL/Teams\nTeiniker'

        self.driver.find_element(By.LINK_TEXT, "Logout").click()


if __name__ == '__main__':
    unittest.main()
