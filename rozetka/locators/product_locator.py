from selenium.webdriver.common.by import By


class ProductPageLocators:

    # product's fields :
    PRODUCT = (By.XPATH, '/html/body/app-root/div/div/rz-category/div/main/rz-catalog/div/div/section/rz-grid/ul/li[1]/rz-catalog-tile/app-goods-tile-default/div/div[2]/a[1]')
    PRODUCT_DESCRIPTION = (By.XPATH, "/html/body/app-root/div/div/rz-product/div/rz-product-top/div/div[1]/h1")

    # feedback's fields :
    FEEDBACKS = (By.XPATH, "/html/body/app-root/div/div/rz-product/div/rz-product-navbar/rz-tabs/div/div/ul/li[3]/a")
    WRITE_FEEDBACK = (By.CLASS_NAME, "button.button.button--medium.button--gray")
    STAR_RATING = (By.XPATH, "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-product-add-comments/div/form/fieldset/div[1]/rz-comment-rating-stars/div/rz-rating/span[5]")
    COMMENT = (By.ID, "comment-text")
    LEAVE_FEEDBACK = (By.XPATH ,"/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-product-add-comments/div/form/fieldset/div[10]/div/button[2]")
    THANK = (By.XPATH, "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-thanks-modal/div/h4")
    PROCESSING = (By.XPATH, "/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-thanks-modal/div/p")
