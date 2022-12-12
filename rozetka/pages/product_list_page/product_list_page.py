from rozetka.pages.base_page import BasePage
from rozetka.locators.product_list_locator import ProductListPageLocators
from rozetka.pages.product_page.product_page import ProductPage
from config.sleeper import wait


class ProductListPage(BasePage):

    def __init__(self, driver):
        self.locator = ProductListPageLocators
        super(ProductListPage, self).__init__(driver)
    
    @property
    def list_products(self):
        return [product for product in self.driver.find_elements(*self.locator.PRODUCT)]
    
    @wait(before=1, after=1)
    def click_product(self, product_idx):
        self.wait_element_to_click(self.list_products[product_idx]).click()
        return ProductPage(self.driver)
