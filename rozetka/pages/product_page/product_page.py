from rozetka.pages.base_page import BasePage
from rozetka.locators.product_locator import ProductPageLocators
from rozetka.pages.product_page.feedback_component import FeedbackComponent
from rozetka.pages.sleeper import wait


class ProductPage(BasePage):
    
    def __init__(self, driver):
        self.locator = ProductPageLocators
        super(ProductPage, self).__init__(driver)
    
    def get_product_description(self):
        return self.driver.find_element(*self.locator.PRODUCT_DESCRIPTION).text
    
    def get_all_feedbacks(self):
        return self.driver.find_element(*self.locator.FEEDBACKS)
    
    @wait(before=1)
    def click_feedbacks(self):
        self.get_all_feedbacks().click()
        return self
    
    def get_write_feedback(self):
        return self.driver.find_element(*self.locator.WRITE_FEEDBACK)
    
    @wait(before=1)
    def click_write_feedback(self):
        self.get_write_feedback().click()
        return FeedbackComponent(self.driver)
