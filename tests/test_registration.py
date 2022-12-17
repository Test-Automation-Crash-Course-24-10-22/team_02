from tests.base_test import BaseTest
from rozetka.pages.home_page.home_page import HomePage


class TestRegistration(BaseTest):
    
    def test_password_length_invalid(self):
        """
        We need to verify how many symbols in password we
        need to create an account.
        """

        home_page = HomePage(self.driver)

        user = {
            "first_name": "користувач",
            "last_name": "користувач",
            "phone": "60 000 00 00",
            "email": "user@gmail.com",
            "password": "11111"
        }

        password_invalid = home_page \
            .move_header() \
            .click_user_icon() \
            .click_register() \
            .enter_first_name(user["first_name"]) \
            .enter_last_name(user["last_name"]) \
            .enter_phone(user["phone"]) \
            .enter_email(user["email"]) \
            .enter_password(user["password"]) \
            .get_min_password()
        
        self.assertEqual(password_invalid, "Не менше 6 символів")
