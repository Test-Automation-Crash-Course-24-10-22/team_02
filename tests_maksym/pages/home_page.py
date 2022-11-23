from selenium.webdriver.common.by import By

from locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.logout_button_xpath = Locators.logout_button_xpath
        self.hamburger_button_xpath = Locators.hamburger_button_xpath
        self.switch_to_RU_xpath = Locators.switch_to_RU_xpath
        self.language_text_xpath = Locators.language_text_xpath
    
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()
    
    def click_left_tab(self):
        self.driver.find_element(By.XPATH, self.hamburger_button_xpath).click()
    
    def click_switch_to_RU(self):
        self.driver.find_element(By.XPATH, self.switch_to_RU_xpath).click()
    
    def get_language_text(self):
        return self.driver.find_element(By.XPATH, self.language_text_xpath).text
