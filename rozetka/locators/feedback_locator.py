from selenium.webdriver.common.by import By


class FeedbackLocators:

    STAR_RATING = (By.XPATH, "(//span[@class='stars__item ng-star-inserted'])[5]")
    COMMENT = (By.ID, "comment-text")
    LEAVE_FEEDBACK = (By.XPATH ,"//rz-single-modal-window//button[@class='button button--medium button--navy']")
    THANK = (By.XPATH, "//rz-thanks-modal//h4[@class='thanks-modal__heading']")
    PROCESSING = (By.XPATH, "//rz-thanks-modal//p[@class='thanks-modal__message']")
