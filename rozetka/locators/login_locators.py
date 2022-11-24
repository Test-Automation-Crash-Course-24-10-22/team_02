from selenium.webdriver.common.by import By


class LoginComponentLocators:
    # login page objects :
    email_input = (By.ID, "auth_email")
    password_input = (By.ID, "auth_pass")
    login_button = (By.XPATH,
                    "/html/body/app-root/div/div/rz-auth-page/div/main/div/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]")
    captcha_verification = (By.ID, "ngrecaptcha-0")
