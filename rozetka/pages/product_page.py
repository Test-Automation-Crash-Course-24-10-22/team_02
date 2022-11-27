import time
from rozetka.pages.base_page import BasePage
from rozetka.locators.product_locator import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        self.locator = ProductPageLocators
        super(ProductPage, self).__init__(driver)
    
    def get_product(self):
        return self.driver.find_element(*self.locator.PRODUCT)
    
    def click_product(self):
        time.sleep(1)
        self.get_product().click()
        return self
    
    def get_product_description(self):
        return self.driver.find_element(*self.locator.PRODUCT_DESCRIPTION).text
