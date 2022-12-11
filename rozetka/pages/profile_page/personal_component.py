import time

from rozetka.pages.base_page import BasePage
from rozetka.locators.personal_locator import PersonalLocators


class PersonalComponent(BasePage):

    def __init__(self, driver):
        self.locator = PersonalLocators
        super(PersonalComponent, self).__init__(driver)

    def get_edit_button(self):
        return self.wait_element_to_click(self.locator.EDIT)
    
    def click_edit(self):
        self.get_edit_button().click()
        return self
    
    def get_first_name(self):
        return self.wait_element_visibility(self.locator.FIRST_NAME)
    
    def enter_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        return self
    
    def get_last_name(self):
        return self.wait_element_visibility(self.locator.LAST_NAME)
    
    def enter_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        return self
    
    def get_save_button(self):
        return self.wait_element_to_click(self.locator.SAVE)
    
    def click_save(self):
        self.get_save_button().click()
        time.sleep(1)
        return self
