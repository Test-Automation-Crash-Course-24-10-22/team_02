import time

from selenium.webdriver.common.by import By

from rozetka.locators.login_locators import LoginComponentLocators
from rozetka.pages.base_page import BasePage


class LoginComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = None
        self.password_input = None
        self.login_button = None
        self.captcha_verification = None

    def get_email_input(self):
        if not self.email_input:
            self.email_input = self.driver.find_element(*LoginComponentLocators.email_input)
        return self.email_input
    def enter_email(self, email):
        self.get_email_input().clear()
        self.get_email_input().send_keys(email)
        time.sleep(1)
        return self

    def get_email_password(self):
        if not self.password_input:
            self.password_input = self.driver.find_element(*LoginComponentLocators.password_input)
        return self.password_input
    
    def enter_password(self, password):
        self.get_email_password().clear()
        self.get_email_password().send_keys(password)
        time.sleep(1)
        return self

    def get_login_button(self):
        if not self.login_button:
            self.login_button = self.driver.find_element(*LoginComponentLocators.login_button)
        return self.login_button
    def click_login(self):
        self.get_login_button.click()
        time.sleep(3)
    
    def captcha_verification(self):
        self.driver.find_element(By.ID, self.captcha_verification_id).click()
