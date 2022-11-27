from selenium.webdriver.common.by import By


class ProductPageLocators:

    PRODUCT = (By.XPATH, '/html/body/app-root/div/div/rz-category/div/main/rz-catalog/div/div/section/rz-grid/ul/li[1]/rz-catalog-tile/app-goods-tile-default/div/div[2]/a[1]')
    PRODUCT_DESCRIPTION = (By.XPATH, "/html/body/app-root/div/div/rz-product/div/rz-product-top/div/div[1]/h1")
