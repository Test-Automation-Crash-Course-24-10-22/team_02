from rozetka.pages.base_page import BasePage
from rozetka.locators.profile_locator import ProfilePageLocators
from rozetka.pages.profile_page.personal_component import PersonalComponent
from rozetka.pages.sleeper import wait
import allure


class ProfilePage(BasePage):

    def __init__(self, driver):
        self.locator = ProfilePageLocators
        super(ProfilePage, self).__init__(driver)

    def get_fields(self):
        fields = self.driver.find_element(*self.locator.PERSONAL_DATA).text.split()
        return fields[0], fields[1]
    
    def get_profile_section(self):
        return self.driver.find_element(*self.locator.PROFILE_SECTION)
    
    @allure.step("Click on the 'Особисті дані' section.")
    @wait(before=1)
    def click_profile_section(self):
        self.get_profile_section().click()
        return PersonalComponent(self.driver)
