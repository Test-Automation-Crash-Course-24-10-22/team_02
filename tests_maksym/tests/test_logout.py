import time
import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
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

        self.assertEqual(driver.get_cookie("login")["value"], EMAIL)

        home = HomePage(driver)
        home.click_logout()
        time.sleep(1)

        self.assertEqual(driver.get_cookie("login")["value"], "deleted")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
