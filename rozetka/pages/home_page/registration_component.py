from rozetka.pages.base_page import BasePage
from rozetka.locators.registration_locator import RegistrationLocators
from rozetka.pages.sleeper import wait
import allure


class RegisterComponent(BasePage):

    def __init__(self, driver):
        self.locator = RegistrationLocators
        super(RegisterComponent, self).__init__(driver)
    
    def get_first_name(self):
        return self.driver.find_element(*self.locator.FIRST_NAME)
    
    @allure.step("Fill your first name in the field 'Ім'я'.")
    @wait(after=1)
    def enter_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        return self
    
    def get_last_name(self):
        return self.driver.find_element(*self.locator.LAST_NAME)
    
    @allure.step("Fill your last name in the field 'Прізвище'.")
    @wait(after=1)
    def enter_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        return self
    
    def get_phone(self):
        return self.driver.find_element(*self.locator.PHONE)
    
    @allure.step("Fill your phone number in the field 'Номер телефону'.")
    @wait(after=1)
    def enter_phone(self, phone):
        self.get_phone().clear()
        self.get_phone().send_keys(phone)
        return self
    
    def get_email(self):
        return self.driver.find_element(*self.locator.EMAIL)
    
    @allure.step("Fill your email address in the field 'Ел. пошта'.")
    @wait(after=1)
    def enter_email(self, email):
        self.get_email().clear()
        self.get_email().send_keys(email)
        return self
    
    def get_password(self):
        return self.driver.find_element(*self.locator.PASSWORD)
    
    @allure.step("Fill your password in the field 'Придумайте пароль'.")
    @wait(after=1)
    def enter_password(self, password):
        self.get_password().clear()
        self.get_password().send_keys(password)
        return self
    
    @allure.step("Get the minimum password length.")
    def get_min_password(self):
        return self.driver.find_element(*self.locator.MIN_PASSWORD).text    
