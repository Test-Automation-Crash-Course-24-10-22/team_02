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
    
    def get_all_feedbacks(self):
        return self.driver.find_element(*self.locator.FEEDBACKS)
    
    def click_feedbacks(self):
        time.sleep(1)
        self.get_all_feedbacks().click()
        return self
    
    def get_write_feedback(self):
        return self.driver.find_element(*self.locator.WRITE_FEEDBACK)
    
    def click_write_feedback(self):
        time.sleep(1)
        self.get_write_feedback().click()
        return self
    
    def get_star_rating(self):
        return self.driver.find_element(*self.locator.STAR_RATING)
    
    def evaluate_star_rating(self):
        time.sleep(1)
        self.get_star_rating().click()
        return self
    
    def get_comment(self):
        return self.driver.find_element(*self.locator.COMMENT)
    
    def enter_comment(self, comment):
        self.get_comment().clear()
        self.get_comment().send_keys(comment)
        return self
    
    def get_leave_feedback(self):
        return self.driver.find_element(*self.locator.LEAVE_FEEDBACK)
    
    def click_leave_feedback(self):
        self.get_leave_feedback().click()
        time.sleep(1)
        return self
    
    def get_thank_text(self):
        return self.driver.find_element(*self.locator.THANK).text
    
    def get_processing_text(self):
        return self.driver.find_element(*self.locator.PROCESSING).text
