from selenium.webdriver.common.by import By

from locators.locators import Locators


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.personal_data_xpath = Locators.personal_data_xpath
        self.edit_xpath = Locators.edit_xpath
        self.first_name_id = Locators.first_name_id
        self.get_first_name_xpath = Locators.get_first_name_xpath
        self.last_name_id = Locators.last_name_id
        self.get_last_name_xpath = Locators.get_last_name_xpath
        self.save_xpath = Locators.save_xpath

    def click_profile_section(self):
        self.driver.find_element(By.XPATH, self.personal_data_xpath).click()
    
    def click_edit(self):
        self.driver.find_element(By.XPATH, self.edit_xpath).click()
    
    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name)
    
    def click_save(self):
        self.driver.find_element(By.XPATH, self.save_xpath).click()
    
    def get_updates(self):
        return self.driver.find_element(By.XPATH, self.get_first_name_xpath).text, \
               self.driver.find_element(By.XPATH, self.get_last_name_xpath).text
