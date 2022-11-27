from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PERSONAL_DATA = (By.XPATH, "/html/body/app-root/div/div/rz-app-cabinet/div/aside/nav/div/a/div[2]/p[1]")
    PROFILE_SECTION = (By.XPATH, '//*[@id="cabinet-content"]/rz-cabinet-personal-information/rz-personal-information-section-header[1]/details/summary/h3')
    EDIT = (By.CLASS_NAME, "button.button.button--medium.button--green.personal-data__edit")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    SAVE = (By.CLASS_NAME, "button.button.button--medium.button--green")
