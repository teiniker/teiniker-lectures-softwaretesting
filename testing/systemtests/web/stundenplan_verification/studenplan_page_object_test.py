import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SchedulePage:
    def __init__(self, driver):
        self.driver = driver

    def get_lecture(self):
        self.driver.find_element(By.NAME, "new_jg").click()
        dropdown = self.driver.find_element(By.NAME, "new_jg")
        dropdown.find_element(By.XPATH, "//option[. = '2020']").click()
        self.driver.find_element(By.CSS_SELECTOR, "select:nth-child(1) > option:nth-child(2)").click()
        self.driver.find_element(By.NAME, "new_date").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(38)").click()
        self.driver.find_element(By.NAME, "new_values").click()       
        self.driver.find_element(By.CSS_SELECTOR, ".event:nth-child(117)").click()
        lecture = self.driver.find_element(By.CSS_SELECTOR, ".event:nth-child(117)").text
        print(lecture)
        return lecture

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://stundenplan.fh-joanneum.at/')
        self.username = ''
        self.password = ''

    def login(self):
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys(self.username)
        self.driver.find_element(By.NAME, "pass").send_keys(self.password)
        self.driver.find_element(By.NAME, "login").click()        
        return SchedulePage(self.driver)


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
