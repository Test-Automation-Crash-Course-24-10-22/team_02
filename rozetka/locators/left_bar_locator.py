from selenium.webdriver.common.by import By


class LeftBarLocators:
    
    text_field = "(//p[@class='side-menu__switch-label ng-tns-c93-1'])"

    RU = (By.XPATH, "//nav//a[contains(text(), 'RU')]")
    LANGUAGE_TEXT = (By.XPATH, f"{text_field}[1]")
    CITY_TEXT = (By.XPATH, f"{text_field}[2]")
