import time
from rozetka.pages.base_page import BasePage
from rozetka.locators.login_locator import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)
    
    def get_email(self):
        return self.driver.find_element(*self.locator.EMAIL)
    
    def enter_email(self, email):
        self.get_email().clear()
        self.get_email().send_keys(email)
        return self

    def get_password(self):
        return self.driver.find_element(*self.locator.PASSWORD)
    
    def enter_password(self, password):
        self.get_password().clear()
        self.get_password().send_keys(password)
        return self

    def get_login_button(self):
        return self.wait_element_to_click(self.locator.SUBMIT)
    
    def click_login(self):
        time.sleep(5)
        self.get_login_button().click()
        return self
    
    def get_captcha(self):
        return self.wait_element_to_click(self.locator.CAPTCHA)
    
    def click_captcha(self):
        self.get_captcha().click()
        return self
