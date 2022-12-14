from selenium.webdriver.common.by import By


class ProductListPageLocators:

    PRODUCT = (By.XPATH, "//a[@class='goods-tile__picture ng-star-inserted']")
    PRODUCTS_TITLE = (By.XPATH, "//h1[@class='catalog-heading ng-star-inserted']")
