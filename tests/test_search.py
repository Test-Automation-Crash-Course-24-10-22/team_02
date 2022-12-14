from tests.base_test import BaseTest
from rozetka.pages.home_page.home_page import HomePage


class TestSearch(BaseTest):

    def test_search_invalid(self):
        """
        We need to verify that search returns proper error
        message after user entered spaces instead of text.
        """

        home_page = HomePage(self.driver)

        search_data = "   "

        header = home_page \
            .move_header() \
            .enter_search(search_data) \
            .click_find()
        
        self.assertEqual(header.get_error_message(), "За заданими параметрами не знайдено жодної моделі")
    
    def test_search_products(self):
        """
        We need to verify that the search functionality can
        find specific products and their titles.
        """

        home_page = HomePage(self.driver)

        found_products = []
        products = ["Планшети", "Комп'ютери", "Телевізори"]

        for product in products:
            home_page.open("/")
            found_products.append(home_page \
                .move_header() \
                .enter_search(product) \
                .click_find() \
                .move_product_list() \
                .get_products_title())
        
        self.assertListEqual(found_products, products)
