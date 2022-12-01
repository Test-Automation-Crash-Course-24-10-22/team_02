from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from rozetka.pages.base_page import BasePage


class ProductListItem(BasePage):

    def __init__(self, driver, root: WebElement):
        super().__init__(driver)
        self.root = root


    def get_heart_button(self) -> WebElement:
        return self.root.find_element(By.XPATH,
                                       "./rz-catalog-tile/app-goods-tile-default/div/div[2]/div[1]/app-goods-wishlist/button")

    def click_heart_button(self):
        self.get_heart_button().click()
