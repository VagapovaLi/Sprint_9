import pytest
import allure

import urls
from pages.main_page import MainPage
from locators.map_locators import MapLocators as Ml
from locators.form_search_locators import FormSearchLocators as Fsl


@allure.feature("Отрисовка маршрута")
class TestRouteFunctionality:

    @allure.story("Отображение точек маршрута на карте")
    @allure.title("Проверка отображения точек маршрута для разных адресов")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37"),
        ("Зубовский бульвар, 37", "Хамовнический Вал, 34")
    ], ids=["From Хамовнический to Зубовский", "From Зубовский to Хамовнический"])

    def test_route_points_displayed_on_map(self, driver, from_address, to_address):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)

        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        assert main_page.check_is_displayed(Ml.END_POINT), "Точка назначения не отображается"
        assert main_page.check_is_displayed(Ml.START_POINT), "Точка отправления не отображается"