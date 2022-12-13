from selenium.webdriver.common.by import By


class HeaderLocators:

    CATALOGUE = (By.XPATH, "//button[@class='button button--medium button--with-icon menu__toggle ng-star-inserted']")
    SEARCH = (By.XPATH, "//input[@class='search-form__input ng-untouched ng-pristine ng-valid']")
    FIND = (By.CLASS_NAME, "button.button.button_color_green.button_size_medium.search-form__submit.ng-star-inserted")
    USER_ICON = (By.XPATH, "(//button[@class='header__button ng-star-inserted'])[1]")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='ng-star-inserted']")
