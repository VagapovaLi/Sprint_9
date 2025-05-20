import pytest
import allure

import urls

from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl


@allure.feature("Отрисовка блока маршрут")
class TestRouteOptionsDisplay:

    @allure.story("Отображение блока маршрута")
    @allure.title("Проверка отображения блока маршрута для разных адресов")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37"),
        ("Зубовский бульвар, 37", "Хамовнический Вал, 34")
    ], ids=["From Хамовнический to Зубовский", "From Зубовский to Хамовнический"])
    def test_add_route_shows_block_with_route_selection(self, driver, from_address, to_address):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)

        route_modes = [Fsl.MODE_OPTIMAL, Fsl.MODE_FAST, Fsl.MODE_CUSTOM]
        for mode in route_modes:
            assert main_page.check_is_displayed(mode), f"Режим {mode} не отображается"


    @allure.story("Отображение блока маршрута")
    @allure.title("Проверка блока маршрута при вводе одинаковых адресов")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Хамовнический Вал, 34"),
        ("Зубовский бульвар, 37", "Зубовский бульвар, 37")
    ], ids=["Same address Хамовнический", "Same address Зубовский"])

    def test_route_block_for_same_address(self, driver, from_address, to_address):
        text_search = "Авто Бесплатно"
        duration_search = "В пути 0 мин."
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, from_address)
        assert text_search == main_page.get_element_text(Fsl.TEXT_RESULT_SEARCH)
        assert duration_search == main_page.get_element_text(Fsl.DURATION_RESULT_SEARCH)