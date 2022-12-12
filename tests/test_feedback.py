from tests.base_test import BaseTest
from rozetka.pages.login_page.login_page import LoginPage
from rozetka.pages.product_list_page.product_list_page import ProductListPage
from config.credentials import EMAIL, PASSWORD


class TestFeedback(BaseTest):

    def test_leave_feedback_valid(self):
        # login into your account :
        login_page = LoginPage(self.driver)
        login_page.open("/signin/")
        login_page \
            .enter_email(EMAIL) \
            .enter_password(PASSWORD) \
            .click_login() \
            .click_captcha() \
            .click_login()
        
        # move to the notebooks section and leave the feedback :
        product_list_page = ProductListPage(self.driver)
        product_list_page.open("/notebooks/c80004/")

        product_number = 0
        comment = "Якісний товар !"

        product_page = product_list_page \
            .click_product(product_number) \
            .click_feedbacks() \
            .click_write_feedback() \
            .evaluate_star_rating() \
            .enter_comment(comment) \
            .click_leave_feedback()
        
        self.assertEqual(product_page.get_thank_text(), "Дякуємо!")
        self.assertEqual(product_page.get_processing_text(), "Ваш відгук буде опубліковано після проходження модерації")
