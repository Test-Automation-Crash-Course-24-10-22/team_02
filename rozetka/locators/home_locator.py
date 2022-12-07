from selenium.webdriver.common.by import By


class HomePageLocators:

    text_field = "(//p[@class='side-menu__switch-label ng-tns-c93-1'])"

    LOGO = (By.XPATH, "//img[contains(@alt, 'Rozetka Logo')]")
    LOGOUT = (By.XPATH, "//li//a[contains(text(), 'Вихід')]")
    HAMBURGER_BUTTON = (By.XPATH, "//button[@class='header__button ng-tns-c93-1']")
    RU = (By.XPATH, "//nav//a[contains(text(), 'RU')]")
    LANGUAGE_TEXT = (By.XPATH, f"{text_field}[1]")
    CITY_TEXT = (By.XPATH, f"{text_field}[2]")
    VIEWED_PRODUCT = (By.XPATH, "//a[@class='tile__title']")
