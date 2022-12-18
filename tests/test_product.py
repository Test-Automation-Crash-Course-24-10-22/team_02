from tests.base_test import BaseTest
from rozetka.pages.home_page.home_page import HomePage
from rozetka.pages.product_list_page.product_list_page import ProductListPage
import allure


class TestViewedProduct(BaseTest):

    @allure.issue(
        "https://github.com/Test-Automation-Crash-Course-24-10-22/team_02/issues/31",
        "Verify the functionality of adding product to the section 'Останні переглянуті товари'")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("""
        We need to check whether the viewed item is added to the
        section "Переглянуті товари".
    """)
    def test_viewed_section(self):
        product_list_page = ProductListPage(self.driver)

        viewed_products = []
        total_products = 3

        for product_number in range(total_products):
            product_list_page.open("/notebooks/c80004/")
            viewed_products.append(product_list_page.click_product(product_number).get_product_description())
        
        home_page = HomePage(self.driver)
        home_page.open("/")
        viewed_products_section = home_page.get_viewed_products()

        self.assertListEqual(viewed_products, viewed_products_section[::-1][:total_products])
