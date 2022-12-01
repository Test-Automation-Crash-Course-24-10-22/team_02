from selenium.webdriver.common.by import By

from rozetka.pages.base_page import BasePage
from rozetka.pages.product_list.product_list_item import ProductListItem


class ProductList(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.list_items = []
        items = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'catalog-grid__cell')]")

        for item in items:
            self.list_items.append(ProductListItem(self.driver, item))
