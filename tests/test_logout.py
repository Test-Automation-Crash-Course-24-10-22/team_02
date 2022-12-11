from tests.base_test import BaseTest
from rozetka.pages.login_page.login_page import LoginPage
from rozetka.pages.home_page.home_page import HomePage
from credentials import EMAIL, PASSWORD


class TestLogout(BaseTest):

    def test_logout_valid(self):
        # login into your account :
        login_page = LoginPage(self.driver)
        login_page.open("/signin/")
        login_page \
            .enter_email(EMAIL) \
            .enter_password(PASSWORD) \
            .click_login() \
            .click_captcha() \
            .click_login()

        # logout from your account :
        home_page = HomePage(self.driver)

        viewed_title_text = "Останні переглянуті товари"

        self.assertEqual(home_page.get_viewed_title(), viewed_title_text)
        self.assertEqual(home_page.get_credentials_cookie(), EMAIL)

        home_page.click_logout()

        self.assertEqual(home_page.get_viewed_title(), viewed_title_text)
        self.assertEqual(home_page.get_credentials_cookie(), "deleted")
