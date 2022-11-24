import time
import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
from credentials import EMAIL, PASSWORD

from rozetka.pages.login_component import LoginComponent
from tests.setup_driver import get_driver


class TestLogout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()

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
    def test_logout_valid2(self):
        login_page = LoginComponent(webdriver)
        login_page.get("https://rozetka.com.ua/ua/signin/")
        login_page\
            .enter_email(EMAIL)\
            .enter_password(PASSWORD)\
            .click_login()

        self.assertEqual(self.driver.get_cookie("login")["value"], EMAIL)

        home = HomePage(self.driver)
        home.click_logout()
        time.sleep(1)

        self.assertEqual(driver.get_cookie("login")["value"], "deleted")

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.close()
            cls.driver.quit()
