from tests.base_test import BaseTest
from rozetka.pages.home_page import HomePage
from rozetka.pages.product_page import ProductPage


class TestViewedProduct(BaseTest):

    product_urls = ["/notebooks/c80004/", "/mobile-phones/c80003/", "/consoles/c80020/"]

    def test_viewed_section(self):
        # see product specifications :
        product_page = ProductPage(self.driver)

        for product_url in self.product_urls:
            product_page.open(product_url)
            viewed_product = product_page.click_product().get_product_description()
    
        # check whether the product is added to the section "viewed products" :
        home_page = HomePage(self.driver)
        home_page.open("/")
        viewed_product_section = home_page.get_viewed_product()

        self.assertEqual(viewed_product, viewed_product_section)
