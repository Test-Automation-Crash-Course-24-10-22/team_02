from selenium.webdriver.common.by import By


class HomePageLocators:

    LOGOUT_BUTTON = (By.XPATH, "//li//a[contains(text(), 'Вихід')]")
    HAMBURGER_BUTTON = (By.XPATH, "//button[@class='header__button ng-tns-c93-1']")
    VIEWED_PRODUCT = (By.XPATH, "//a[@class='tile__title']")
    VIEWED_TITLE = (By.XPATH, "//h2[@class='main-goods__heading ng-star-inserted']")
