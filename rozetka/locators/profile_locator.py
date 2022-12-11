from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PERSONAL_DATA = (By.XPATH, "//p[@class='cabinet-user__name']")
    PROFILE_SECTION = (By.XPATH, "//h3[@class='personal-section__heading']")
