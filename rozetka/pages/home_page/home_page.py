import time

from rozetka.pages.base_page import BasePage
from rozetka.locators.home_locator import HomePageLocators
from rozetka.pages.home_page.left_bar_component import LeftBarComponent
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = HomePageLocators
        super(HomePage, self).__init__(driver)
    
    def get_logout(self):
        return self.wait_element_to_click(self.locator.LOGOUT_BUTTON)
    
    def click_logout(self):
        self.get_logout().click()
        time.sleep(1)
        return self
    
    def get_left_tab(self):
        return self.wait_element_to_click(self.locator.HAMBURGER_BUTTON)
    
    def click_left_tab(self):
        self.get_left_tab().click()
        return LeftBarComponent(self.driver)
    
    def get_viewed_title(self):
        return self.wait_element_visibility(self.locator.VIEWED_TITLE).text
    
    def get_viewed_product(self):
        return self.wait_element_visibility(self.locator.VIEWED_PRODUCT).text
    
    def get_credentials_cookie(self):
        return WebDriverWait(self.driver, 10).until(lambda d: d.get_cookie('login'))['value']
