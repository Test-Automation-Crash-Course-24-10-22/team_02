from tests.base_test import BaseTest
from rozetka.pages.home_page import HomePage


class TestLanguageSwitch(BaseTest):

    def test_from_UK_to_RU(self):
        home_page = HomePage(self.driver)
        home_page.click_left_tab()

        self.assertEqual(home_page.get_language_text(), "Мова")
        self.assertEqual(home_page.get_city_text(), "Місто")

        home_page \
            .click_switch_to_RU() \
            .click_left_tab()
        
        self.assertEqual(home_page.get_language_text(), "Язык")
        self.assertEqual(home_page.get_city_text(), "Город")
