from selenium.webdriver.common.by import By

from locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_id = Locators.email_id
        self.password_id = Locators.password_id
        self.login_button_xpath = Locators.login_button_xpath
        self.captcha_verification_id = Locators.captcha_verification_id
    
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
    
    def captcha_verification(self):
        self.driver.find_element(By.ID, self.captcha_verification_id).click()
