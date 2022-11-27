import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=cls.options, service=Service(ChromeDriverManager().install()))
        cls.driver.get("https://rozetka.com.ua/ua/")
        cls.driver.implicitly_wait(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
