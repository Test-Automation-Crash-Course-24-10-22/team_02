import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    SELENIUM_GRID = "http://172.18.0.2:4444/wd/hub"
    ROZETKA_SITE = "http://rozetka.com.ua/ua"

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()

        cls.options.add_argument('--ignore-ssl-errors=yes')
        cls.options.add_argument('--ignore-certificate-errors')
        cls.options.add_argument('--no-sandbox')
        cls.options.add_argument('--disable-dev-shm-usage')

        cls.driver = webdriver.Remote(
            command_executor=cls.SELENIUM_GRID,
            options=cls.options
        )

        cls.driver.maximize_window()
        cls.driver.get(cls.ROZETKA_SITE)
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
