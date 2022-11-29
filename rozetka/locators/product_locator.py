from selenium.webdriver.common.by import By


class ProductPageLocators:

    # product's fields :
    PRODUCT = (By.XPATH, "(//a[@class='goods-tile__picture ng-star-inserted'])[1]")
    PRODUCT_DESCRIPTION = (By.XPATH, "//h1[@class='product__title']")

    # feedback's fields :
    FEEDBACKS = (By.XPATH, "//a[@class='tabs__link' and text()=' Відгуки ']")
    WRITE_FEEDBACK = (By.CLASS_NAME, "button.button.button--medium.button--gray")
    STAR_RATING = (By.XPATH, "(//span[@class='stars__item ng-star-inserted'])[5]")
    COMMENT = (By.ID, "comment-text")
    LEAVE_FEEDBACK = (By.XPATH ,"//button[contains(text(), ' Залишити відгук ')]")
    THANK = (By.XPATH, "//rz-thanks-modal//h4[@class='thanks-modal__heading']")
    PROCESSING = (By.XPATH, "//rz-thanks-modal//p[@class='thanks-modal__message']")
