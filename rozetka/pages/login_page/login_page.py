from rozetka.pages.base_page import BasePage
from rozetka.locators.login_locator import LoginPageLocators
from rozetka.pages.sleeper import wait
import allure
from allure_commons.types import AttachmentType


class LoginPage(BasePage):

    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)
    
    def get_email(self):
        return self.driver.find_element(*self.locator.EMAIL)
    
    @allure.step('In order to log in : Enter your email address.')
    @wait(after=1)
    def enter_email(self, email):
        self.get_email().clear()
        self.get_email().send_keys(email)
        return self

    def get_password(self):
        return self.driver.find_element(*self.locator.PASSWORD)
    
    @allure.step('Enter your password.')
    @wait(after=1)
    def enter_password(self, password):
        self.get_password().clear()
        self.get_password().send_keys(password)
        return self

    def get_login_button(self):
        return self.driver.find_element(*self.locator.SUBMIT)
    
    @allure.step('Click the login button.')
    @wait(before=1, after=1)
    def click_login(self):
        self.get_login_button().click()
        return self
    
    def get_captcha(self):
        return self.driver.find_element(*self.locator.CAPTCHA)
    
    @allure.step('Click the captcha button (Check for robot).')
    @wait(before=1.5)
    def click_captcha(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="CAPTCHA-verification", attachment_type=AttachmentType.PNG)
        self.get_captcha().click()
        return self
