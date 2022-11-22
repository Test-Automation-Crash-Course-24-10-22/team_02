from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.logout_button_xpath = "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[2]/ul/li[14]/a"
    
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()
