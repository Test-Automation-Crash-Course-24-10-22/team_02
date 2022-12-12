from selenium.webdriver.common.by import By


class FeedbackLocators:

    STAR_RATING = (By.XPATH, "(//span[@class='stars__item ng-star-inserted'])[5]")
    COMMENT = (By.ID, "comment-text")
    LEAVE_FEEDBACK = (By.XPATH ,"//button[contains(text(), ' Залишити відгук ')]")
    THANK = (By.XPATH, "//rz-thanks-modal//h4[@class='thanks-modal__heading']")
    PROCESSING = (By.XPATH, "//rz-thanks-modal//p[@class='thanks-modal__message']")
