from tests.base_test import BaseTest
from rozetka.pages.home_page.home_page import HomePage
import allure


class TestLanguageSwitch(BaseTest):

    @allure.issue(
        "https://github.com/Test-Automation-Crash-Course-24-10-22/team_02/issues/28",
        "Verify that the information on the left panel is translated into Russian language")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("""
        This test case verifies that the text on the left panel elements is 
        translated into the chosen language after switching the language toggle.
    """)
    def test_from_UK_to_RU(self):
        home_page = HomePage(self.driver)

        left_tab_first_click = home_page.click_left_bar()

        self.assertEqual(left_tab_first_click.get_language_text(), "Мова")
        self.assertEqual(left_tab_first_click.get_city_text(), "Місто")
        
        left_tab_first_click.click_switch_to_RU()

        left_tab_second_click = home_page.click_left_bar()

        self.assertEqual(left_tab_second_click.get_language_text(), "Язык")
        self.assertEqual(left_tab_second_click.get_city_text(), "Город")
