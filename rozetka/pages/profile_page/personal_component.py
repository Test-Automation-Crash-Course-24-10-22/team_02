from rozetka.pages.base_page import BasePage
from rozetka.locators.personal_locator import PersonalLocators
from rozetka.pages.sleeper import wait
import allure


class PersonalComponent(BasePage):

    def __init__(self, driver):
        self.locator = PersonalLocators
        super(PersonalComponent, self).__init__(driver)

    def get_edit_button(self):
        return self.driver.find_element(*self.locator.EDIT)
    
    @allure.step("Click on the 'Редагувати' button.")
    @wait(before=1)
    def click_edit(self):
        self.get_edit_button().click()
        return self
    
    def get_first_name(self):
        return self.driver.find_element(*self.locator.FIRST_NAME)
    
    @allure.step("Fill your new first name in the field 'Ім'я'.")
    @wait(after=1)
    def enter_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        return self
    
    def get_last_name(self):
        return self.driver.find_element(*self.locator.LAST_NAME)
    
    @allure.step("Fill your new last name in the field 'Прізвище'.")
    @wait(after=1)
    def enter_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        return self
    
    def get_save_button(self):
        return self.driver.find_element(*self.locator.SAVE)
    
    @allure.step("After that click on the 'Зберегти' button.")
    @wait(after=1)
    def click_save(self):
        self.get_save_button().click()
        return self
