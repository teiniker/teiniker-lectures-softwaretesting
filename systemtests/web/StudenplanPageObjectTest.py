import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SchedulePage:
    def __init__(self, driver):
        self.driver = driver

    def get_lectures(self):
        lectures = [self.driver.find_element(By.CSS_SELECTOR, ".event:nth-child(116)").text]
        return lectures

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
        return SchedulePage(self.driver)


class SeleniumTest(unittest.TestCase):

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
