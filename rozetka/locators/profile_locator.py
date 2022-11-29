from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PERSONAL_DATA = (By.XPATH, "//p[@class='cabinet-user__name']")
    PROFILE_SECTION = (By.XPATH, "//h3[@class='personal-section__heading']")
    EDIT = (By.CLASS_NAME, "button.button.button--medium.button--green.personal-data__edit")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    SAVE = (By.CLASS_NAME, "button.button.button--medium.button--green")
