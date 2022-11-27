import time
from rozetka.pages.base_page import BasePage
from rozetka.locators.home_locator import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = HomePageLocators
        super(HomePage, self).__init__(driver)
    
    def get_logout(self):
        return self.driver.find_element(*self.locator.LOGOUT)
    
    def click_logout(self):
        self.get_logout().click()
        time.sleep(1)
        return self
    
    def get_left_tab(self):
        return self.driver.find_element(*self.locator.HAMBURGER_BUTTON)
    
    def click_left_tab(self):
        self.get_left_tab().click()
        time.sleep(1)
        return self
    
    def get_switch_RU(self):
        return self.driver.find_element(*self.locator.RU)
    
    def click_switch_to_RU(self):
        self.get_switch_RU().click()
        time.sleep(1)
        return self
    
    def get_language_text(self):
        return self.driver.find_element(*self.locator.LANGUAGE_TEXT).text
    
    def get_city_text(self):
        return self.driver.find_element(*self.locator.CITY_TEXT).text
    
    def get_viewed_product(self):
        return self.driver.find_element(*self.locator.VIEWED_PRODUCT).text
