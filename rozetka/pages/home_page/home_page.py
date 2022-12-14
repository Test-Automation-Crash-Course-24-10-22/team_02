from rozetka.pages.base_page import BasePage
from rozetka.locators.home_locator import HomePageLocators
from rozetka.pages.home_page.header_component import HeaderComponent
from rozetka.pages.home_page.left_bar_component import LeftBarComponent
from rozetka.pages.sleeper import wait


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = HomePageLocators
        super(HomePage, self).__init__(driver)
    
    def move_header(self):
        return HeaderComponent(self.driver)

    def get_logout(self):
        return self.driver.find_element(*self.locator.LOGOUT_BUTTON)
    
    @wait(after=1)
    def click_logout(self):
        self.get_logout().click()
        return self
    
    def get_left_bar(self):
        return self.driver.find_element(*self.locator.HAMBURGER_BUTTON)
    
    @wait(after=1)
    def click_left_bar(self):
        self.get_left_bar().click()
        return LeftBarComponent(self.driver)
    
    def get_viewed_title(self):
        return self.driver.find_element(*self.locator.VIEWED_TITLE).text
    
    def get_viewed_products(self):
        return [product.text for product in self.driver.find_elements(*self.locator.VIEWED_PRODUCT)]
    
    @wait(before=1)
    def get_credentials_cookie(self):
        return self.driver.get_cookie("login")["value"]
