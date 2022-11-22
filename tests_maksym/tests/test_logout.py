import time
import unittest

from selenium import webdriver

from pom.login_page import LoginPage
from pom.home_page import HomePage
from credentials import EMAIL, PASSWORD


class TestLogout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()
    
    def test_logout_valid(self):
        driver = self.driver
        driver.get("https://rozetka.com.ua/ua/signin/")

        login = LoginPage(driver)
        login.enter_email(EMAIL)
        time.sleep(1)
        login.enter_password(PASSWORD)
        time.sleep(1)
        login.click_login()
        time.sleep(1)
        login.captcha_verification()
        time.sleep(1)
        login.click_login()
        time.sleep(1)

        home = HomePage(driver)
        home.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
