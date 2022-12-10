from tests.base_test import BaseTest
from rozetka.pages.home_page.home_page import HomePage


class TestLanguageSwitch(BaseTest):

    def test_from_UK_to_RU(self):
        home_page = HomePage(self.driver)

        left_tab_first_click = home_page.click_left_tab()

        self.assertEqual(left_tab_first_click.get_language_text(), "Мова")
        self.assertEqual(left_tab_first_click.get_city_text(), "Місто")
        
        left_tab_first_click.click_switch_to_RU()

        left_tab_second_click = home_page.click_left_tab()

        self.assertEqual(left_tab_second_click.get_language_text(), "Язык")
        self.assertEqual(left_tab_second_click.get_city_text(), "Город")
