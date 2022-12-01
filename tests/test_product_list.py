import time

from rozetka.pages.product_list.product_list import ProductList
from tests.base_test import BaseTest

class TestProductList(BaseTest):

    def test_productList(self):

        self.driver.get("https://rozetka.com.ua/ua/consoles/c80020/")
        pl = ProductList(self.driver)

        pl.list_items[3].click_heart_button()
        time.sleep(3)
        pl.list_items[3].click_heart_button()
        time.sleep(3)
        pl.list_items[3].click_heart_button()
        time.sleep(3)
        pl.list_items[3].click_heart_button()
        time.sleep(3)
