from selenium.webdriver.common.by import By


class RegistrationLocators:

    FIRST_NAME = (By.ID, "registerUserName")
    LAST_NAME = (By.ID, "registerUserSurname")
    PHONE = (By.ID, "registerUserPhone")
    EMAIL = (By.ID, "registerUserEmail")
    PASSWORD = (By.ID, "registerUserPassword")
    MIN_PASSWORD = (By.XPATH, "(//form//p[@class='errors-list__text'])[3]")
