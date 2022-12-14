from selenium.webdriver.common.by import By


class PersonalLocators:

    EDIT = (By.CLASS_NAME, "button.button.button--medium.button--green.personal-data__edit")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    SAVE = (By.CLASS_NAME, "button.button.button--medium.button--green")
