import time
from rozetka.pages.base_page import BasePage
from rozetka.locators.profile_locator import ProfilePageLocators


class ProfilePage(BasePage):

    def __init__(self, driver):
        self.locator = ProfilePageLocators
        super(ProfilePage, self).__init__(driver)
    
    def get_profile_section(self):
        return self.driver.find_element(*self.locator.PROFILE_SECTION)
    
    def click_profile_section(self):
        self.get_profile_section().click()
        return self
    
    def get_edit_button(self):
        return self.driver.find_element(*self.locator.EDIT)
    
    def click_edit(self):
        time.sleep(1)
        self.get_edit_button().click()
        return self
    
    def get_fields(self):
        fields = self.driver.find_element(*self.locator.PERSONAL_DATA).text.split()
        return fields[0], fields[1]
    
    def get_first_name(self):
        return self.driver.find_element(*self.locator.FIRST_NAME)
    
    def enter_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        time.sleep(1)
        return self
    
    def get_last_name(self):
        return self.driver.find_element(*self.locator.LAST_NAME)
    
    def enter_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        time.sleep(1)
        return self
    
    def get_save_button(self):
        return self.driver.find_element(*self.locator.SAVE)
    
    def click_save(self):
        self.get_save_button().click()
        time.sleep(1)
