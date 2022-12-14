from rozetka.pages.base_page import BasePage
from rozetka.locators.product_list_locator import ProductListPageLocators
from rozetka.pages.product_page.product_page import ProductPage
from rozetka.pages.sleeper import wait
import allure


class ProductListPage(BasePage):

    def __init__(self, driver):
        self.locator = ProductListPageLocators
        super(ProductListPage, self).__init__(driver)
    
    @property
    def list_products(self):
        return [product for product in self.driver.find_elements(*self.locator.PRODUCT)]
    
    @allure.step("Get the products title.")
    @wait(before=2)
    def get_products_title(self):
        return self.driver.find_element(*self.locator.PRODUCTS_TITLE).text
    
    @allure.step("Click on the first product (in my case it's a notebook).")
    @wait(before=1, after=1)
    def click_product(self, product_idx):
        self.wait_element_to_click(self.list_products[product_idx]).click()
        return ProductPage(self.driver)
