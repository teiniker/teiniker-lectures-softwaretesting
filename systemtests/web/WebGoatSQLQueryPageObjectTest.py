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

    def navigateToSqlInjectionIntro(self):
        self.driver.get("http://localhost:8080/WebGoat/start.mvc#lesson/SqlInjection.lesson/1")
        return SQLInjectionIntroPage(self.driver)

    def logout(self):
        self.driver.get("http://localhost:8080/WebGoat/logout")


class SQLInjectionIntroPage:
    def __init__(self, driver):
        self.driver = driver

    def sqlQuery(self, query):
        self.query = query

    def submit(self):
        self.driver.find_element(By.NAME, "query").send_keys(self.query)
        self.driver.find_element(By.CSS_SELECTOR, ".lesson-page-wrapper:nth-child(6) button").click()
        time.sleep(5)   # to see the result of the query
        self.driver.find_element(By.CSS_SELECTOR, ".lesson-page-wrapper:nth-child(6) .attack-feedback").click()
        return self.driver.find_element(By.CSS_SELECTOR, ".attack-feedback > .feedback-positive").text


class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        login_page = LoginPage(self.driver)
        login_page.username('student')
        login_page.password('student')
        self.main_page = login_page.login()

    def tearDown(self):
        self.main_page.logout()
        self.driver.quit()


    def testSqlQuery(self):
        sql_page = self.main_page.navigateToSqlInjectionIntro()
        sql_page.sqlQuery("select department from employees where userid=96134")
        text = sql_page.submit()
        self.assertEqual("You have succeeded!", text)


if __name__ == '__main__':
    unittest.main()
