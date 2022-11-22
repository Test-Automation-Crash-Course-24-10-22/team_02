from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_id = "auth_email"
        self.password_id = "auth_pass"
        self.login_button_xpath = "/html/body/app-root/div/div/rz-auth-page/div/main/div/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]"
        self.captcha_verification_id = "ngrecaptcha-0"
    
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
    
    def captcha_verification(self):
        self.driver.find_element(By.ID, self.captcha_verification_id).click()
