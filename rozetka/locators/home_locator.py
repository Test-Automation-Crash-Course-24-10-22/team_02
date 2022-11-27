from selenium.webdriver.common.by import By


class HomePageLocators:

    LOGOUT = (By.XPATH, "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[2]/ul/li[14]/a")
    HAMBURGER_BUTTON = (By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/rz-mobile-user-menu/button')
    RU = (By.XPATH, '//*[@id="cdk-overlay-0"]/nav/div/div[2]/ul[2]/li[1]/div[1]/rz-lang/ul/li[1]/a')
    LANGUAGE_TEXT = (By.XPATH, '//*[@id="cdk-overlay-0"]/nav/div/div[2]/ul[2]/li[1]/div[1]/p')
    CITY_TEXT = (By.XPATH, '//*[@id="cdk-overlay-0"]/nav/div/div[2]/ul[2]/li[1]/div[2]/p')
