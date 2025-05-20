import time

import pytest
import allure
import urls
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl




@allure.feature("Функциональность маршрутов")
class TestRouteSwitching:
    @allure.story("Переключение между видами маршрута")
    @allure.title("Проверка переключения между Быстрым и Оптимальным маршрутом")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_when_switching_between_route_types(self, driver, from_address, to_address):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        optimal_text = main_page.get_element_text(Fsl.TEXT_RESULT_SEARCH)
        optimal_duration = main_page.get_element_text(Fsl.DURATION_RESULT_SEARCH)
        main_page.click_element(Fsl.MODE_OPTIMAL)

        assert main_page.is_tab_active_route(Fsl.MODE_OPTIMAL), "Таб оптимальный маршрута не активен"
        assert (optimal_text != main_page.get_element_text(Fsl.TEXT_RESULT_SEARCH)
                or optimal_duration != main_page.get_element_text(
                    Fsl.DURATION_RESULT_SEARCH)), "Стоимость и длительность не изменилась"



    @allure.story("Переключение между видами маршрута")
    @allure.title("Проверка переключения на вид маршрута 'Свой'")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_when_switching_view_yours(self, driver, from_address, to_address):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        main_page.click_element(Fsl.MODE_CUSTOM)

        assert main_page.is_tab_active_route(Fsl.MODE_CUSTOM), "Таб пользовательского маршрута не активен"
        for transport_type in [Fsl.TRANSPORT_CAR, Fsl.TRANSPORT_WALK,
                               Fsl.TRANSPORT_TAXI, Fsl.TRANSPORT_BIKE,
                               Fsl.TRANSPORT_SCOOTER, Fsl.TRANSPORT_DRIVE]:
            assert main_page.check_is_displayed(
                transport_type), f"Тип передвижения {transport_type} недоступен"



    @allure.story("Доступность кнопок заказа")
    @allure.title("Проверка активности кнопки 'Вызвать такси' для быстрого маршрута")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_taxi_available_in_fast_mode(self, driver, from_address, to_address):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        main_page.click_element(Fsl.MODE_FAST)
        main_page.click_element(Fsl.BUTTON_CALL_TAXI)

        for tariff_type in [Fsl.WORKER_TARIFF, Fsl.SLEEPY_TARIFF,
                            Fsl.VACATION_TARIFF, Fsl.TALKATIVE_TARIFF,
                            Fsl.COMFORTING_TARIFF, Fsl.GLOSSY_TARIFF]:
            assert main_page.check_is_displayed(
                tariff_type)

    @allure.story("Доступность кнопок заказа")
    @allure.title("Проверка активности кнопки 'Забронировать' для типа 'Драйв'")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37")
    ])
    def test_book_button_availability_for_drive_type(self, driver, from_address, to_address):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        main_page.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        main_page.click_element(Fsl.MODE_CUSTOM)
        main_page.click_element(Fsl.TRANSPORT_DRIVE)
        main_page.click_element(Fsl.BUTTON_RESERVATION_DRIVE)
        for tariff_type in [Fsl.EVERYDAY_TARIFF, Fsl.CAMPING_TARIFF,
                            Fsl.LUXURY_TARIFF]:
            assert main_page.check_is_displayed(
                tariff_type)


