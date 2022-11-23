import time

from selenium.webdriver.common.by import By

from locators.locators import Locators


class ProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.personal_data_xpath = Locators.personal_data_xpath
        self.edit_xpath = Locators.edit_xpath
        self.get_old_first_last_name_xpath = Locators.get_old_first_last_name_xpath
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
    
    def update_profile(self, first_name, last_name):
        self.click_edit()
        time.sleep(1)
        self.enter_first_name(first_name)
        time.sleep(1)
        self.enter_last_name(last_name)
        time.sleep(1)
        self.click_save()
        time.sleep(1)
    
    def get_old_fields(self):
        fields = self.driver.find_element(By.XPATH, self.get_old_first_last_name_xpath).text.split()
        return fields[0], fields[1]
    
    def get_fields(self):
        return self.driver.find_element(By.XPATH, self.get_first_name_xpath).text, \
               self.driver.find_element(By.XPATH, self.get_last_name_xpath).text
