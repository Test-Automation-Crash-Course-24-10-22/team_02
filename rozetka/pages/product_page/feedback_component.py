from rozetka.pages.base_page import BasePage
from rozetka.locators.feedback_locator import FeedbackLocators
from config.sleeper import wait


class FeedbackComponent(BasePage):

    def __init__(self, driver):
        self.locator = FeedbackLocators
        super(FeedbackComponent, self).__init__(driver)
    
    def get_star_rating(self):
        return self.driver.find_element(*self.locator.STAR_RATING)
    
    @wait(before=1)
    def evaluate_star_rating(self):
        self.get_star_rating().click()
        return self
    
    def get_comment(self):
        return self.driver.find_element(*self.locator.COMMENT)
    
    @wait(after=1)
    def enter_comment(self, comment):
        self.get_comment().clear()
        self.get_comment().send_keys(comment)
        return self
    
    def get_leave_feedback(self):
        return self.driver.find_element(*self.locator.LEAVE_FEEDBACK)
    
    @wait(after=1)
    def click_leave_feedback(self):
        self.get_leave_feedback().click()
        return self
    
    def get_thank_text(self):
        return self.driver.find_element(*self.locator.THANK).text
    
    def get_processing_text(self):
        return self.driver.find_element(*self.locator.PROCESSING).text
