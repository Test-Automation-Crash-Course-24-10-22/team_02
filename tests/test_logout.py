from tests.base_test import BaseTest
from rozetka.pages.login_page import LoginPage
from rozetka.pages.home_page import HomePage
from credentials import EMAIL, PASSWORD


class TestLogout(BaseTest):

    def test_logout_valid(self):
        # login into your account :
        login_page = LoginPage(self.driver)
        login_page.open("signin/")
        login_page \
            .enter_email(EMAIL) \
            .enter_password(PASSWORD) \
            .click_login() \
            .click_captcha() \
            .click_login()

        self.assertEqual(self.driver.get_cookie("login")["value"], EMAIL)

        # logout from your account :
        home_page = HomePage(self.driver)
        home_page.click_logout()

        self.assertEqual(self.driver.get_cookie("login")["value"], "deleted")
