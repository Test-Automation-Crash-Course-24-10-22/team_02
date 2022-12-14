from selenium.webdriver.common.by import By


class ProductPageLocators:

    PRODUCT_DESCRIPTION = (By.XPATH, "//h1[@class='product__title']")
    FEEDBACKS = (By.XPATH, "//a[@class='tabs__link' and text()=' Відгуки ']")
    WRITE_FEEDBACK = (By.CLASS_NAME, "button.button.button--medium.button--gray")
