import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from credentials import EMAIL, PASSWORD


class TestLogout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://rozetka.com.ua")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
    
    def test_logout(self):
        # login functionality :
        user_icon = self.driver.find_element(By.CSS_SELECTOR, "button.header__button.ng-star-inserted")
        user_icon.click()

        email = self.driver.find_element(By.ID, "auth_email")
        email.send_keys(EMAIL)

        password = self.driver.find_element(By.ID, "auth_pass")
        password.send_keys(PASSWORD)

        login = self.driver.find_element(By.CSS_SELECTOR, "button.button.button--large.button--green.auth-modal__submit.ng-star-inserted")
        login.click()
        time.sleep(1)

        verify = self.driver.find_element(By.ID, "ngrecaptcha-0")
        verify.click()
        time.sleep(1)

        login.click()
        time.sleep(1)

        self.assertEqual(self.driver.get_cookie('login')['value'], EMAIL)
        time.sleep(1)

        # logout functionality :
        logout = self.driver.find_element(By.LINK_TEXT, "Вихід")
        logout.click()
        time.sleep(1)

        self.assertEqual(self.driver.get_cookie('login')['value'], 'deleted')


if __name__ == '__main__':
    unittest.main()
