from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL = (By.ID, "auth_email")
    PASSWORD = (By.ID, "auth_pass")
    SUBMIT = (By.CLASS_NAME, "button.button.button--large.button--green.auth-modal__submit.ng-star-inserted")
    CAPTCHA = (By.ID, "ngrecaptcha-0")
