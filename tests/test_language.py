import time
import unittest

from selenium import webdriver

from pages.home_page import HomePage


class TestLanguageSwitch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()
    
    def test_from_UK_to_RU(self):
        driver = self.driver
        driver.get("https://rozetka.com.ua")

        home = HomePage(driver)
        home.click_left_tab()
        time.sleep(1)
        home.click_switch_to_RU()
        time.sleep(1)
        home.click_left_tab()
        time.sleep(1)

        self.assertEqual(home.get_language_text(), "Язык")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
