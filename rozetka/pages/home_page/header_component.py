from rozetka.pages.base_page import BasePage
from rozetka.locators.header_locator import HeaderLocators
from rozetka.pages.home_page.registration_component import RegisterComponent
from rozetka.pages.product_list_page.product_list_page import ProductListPage
from rozetka.pages.sleeper import wait


class HeaderComponent(BasePage):

    def __init__(self, driver):
        self.locator = HeaderLocators
        super(HeaderComponent, self).__init__(driver)
    
    def get_search(self):
        return self.driver.find_element(*self.locator.SEARCH)
    
    @wait(after=1)
    def enter_search(self, input_data):
        self.get_search().clear()
        self.get_search().send_keys(input_data)
        return self
    
    def get_find(self):
        return self.driver.find_element(*self.locator.FIND)
    
    @wait(after=1)
    def click_find(self):
        self.get_find().click()
        return self
    
    def get_user_icon(self):
        return self.driver.find_element(*self.locator.USER_ICON)
    
    @wait(before=1)
    def click_user_icon(self):
        self.get_user_icon().click()
        return self

    def get_register(self):
        return self.driver.find_element(*self.locator.REGISTER)
    
    @wait(before=1)
    def click_register(self):
        self.get_register().click()
        return RegisterComponent(self.driver)
    
    def get_error_message(self):
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text
    
    def move_product_list(self):
        return ProductListPage(self.driver)