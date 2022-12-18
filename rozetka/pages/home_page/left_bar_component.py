from rozetka.pages.base_page import BasePage
from rozetka.locators.left_bar_locator import LeftBarLocators
from rozetka.pages.sleeper import wait
import allure


class LeftBarComponent(BasePage):

    def __init__(self, driver):
        self.locator = LeftBarLocators
        super(LeftBarComponent, self).__init__(driver)
    
    def get_switch_RU(self):
        return self.driver.find_element(*self.locator.RU)
    
    @allure.step("Move to the section 'Мова' and click on the 'RU' button.")
    @wait(after=1)
    def click_switch_to_RU(self):
        self.get_switch_RU().click()
        return self
    
    def get_language_text(self):
        return self.driver.find_element(*self.locator.LANGUAGE_TEXT).text
    
    def get_city_text(self):
        return self.driver.find_element(*self.locator.CITY_TEXT).text
