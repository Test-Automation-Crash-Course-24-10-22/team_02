import time
import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from credentials import EMAIL, PASSWORD


class TestProfile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()
    
    def test_update_profile_valid(self):
        driver_login = self.driver
        driver_login.get("https://rozetka.com.ua/ua/signin/")

        login = LoginPage(driver_login)
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

        driver_profile = self.driver
        driver_profile.get("https://rozetka.com.ua/ua/cabinet/personal-information")
        time.sleep(1)

        profile = ProfilePage(driver_profile)
        
        old_first_name, old_last_name = profile.get_old_fields()
        new_first_name, new_last_name = "нові дані", "нові дані"

        profile.click_profile_section()
        profile.update_profile(new_first_name, new_last_name)

        self.assertEqual(profile.get_fields(), (new_first_name, new_last_name))

        profile.update_profile(old_first_name, old_last_name)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
