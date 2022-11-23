
class Locators:

    # login page objects :
    email_id = "auth_email"
    password_id = "auth_pass"
    login_button_xpath = "/html/body/app-root/div/div/rz-auth-page/div/main/div/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[1]"
    captcha_verification_id = "ngrecaptcha-0"

    # home page objects :
    logout_button_xpath = "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[2]/ul/li[14]/a"
    hamburger_button_xpath = "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/rz-mobile-user-menu/button"
    switch_to_RU_xpath = '//*[@id="cdk-overlay-0"]/nav/div/div[2]/ul[2]/li[1]/div[1]/rz-lang/ul/li[1]/a'
    language_text_xpath = '//*[@id="cdk-overlay-0"]/nav/div/div[2]/ul[2]/li[1]/div[1]/p'

    # profile page objects :
    personal_data_xpath = '//*[@id="cabinet-content"]/rz-cabinet-personal-information/rz-personal-information-section-header[1]/details/summary'
    edit_xpath = '//*[@id="cabinet-content"]/rz-cabinet-personal-information/rz-personal-information-section-header[1]/details/div/rz-cabinet-user-information/form/div/div/button'
    first_name_id = "firstName"
    last_name_id = "lastName"
    save_xpath = '//*[@id="cabinet-content"]/rz-cabinet-personal-information/rz-personal-information-section-header[1]/details/div/rz-cabinet-user-information/form/div/div/button[1]'
    get_first_name_xpath = '//*[@id="cabinet-content"]/rz-cabinet-personal-information/rz-personal-information-section-header[1]/details/div/rz-cabinet-user-information/form/div/ul/li[2]/p'
    get_last_name_xpath = '//*[@id="cabinet-content"]/rz-cabinet-personal-information/rz-personal-information-section-header[1]/details/div/rz-cabinet-user-information/form/div/ul/li[1]/p'
