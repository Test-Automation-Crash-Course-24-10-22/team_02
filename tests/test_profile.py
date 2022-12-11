from tests.base_test import BaseTest
from rozetka.pages.login_page.login_page import LoginPage
from rozetka.pages.profile_page.profile_page import ProfilePage
from credentials import EMAIL, PASSWORD


class TestProfile(BaseTest):

    def test_update_profile_valid(self):
        # login into your account :
        login_page = LoginPage(self.driver)
        login_page.open("/signin/")
        login_page \
            .enter_email(EMAIL) \
            .enter_password(PASSWORD) \
            .click_login() \
            .click_captcha() \
            .click_login()
        
        # update your profile :
        profile_page = ProfilePage(self.driver)
        profile_page.open("/cabinet/personal-information/")
        
        old_first_name, old_last_name = profile_page.get_fields()
        new_first_name, new_last_name = "НовіДані", "НовіДані"

        renewal_page = profile_page \
            .click_profile_section() \
            .click_edit() \
            .enter_first_name(new_first_name) \
            .enter_last_name(new_last_name) \
            .click_save()
        
        self.assertEqual(profile_page.get_fields(), (new_first_name, new_last_name))

        renewal_page \
            .click_edit() \
            .enter_first_name(old_first_name) \
            .enter_last_name(old_last_name) \
            .click_save()
        
        self.assertEqual(profile_page.get_fields(), (old_first_name, old_last_name))
