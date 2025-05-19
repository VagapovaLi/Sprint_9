import time

import allure

import pytest
from tests.conftest import main_page
from locators.main_page_locators import MainPageLocators
from utils.trip_mode import TripMode

class TestMainPage:
    ADDRESS_A = "Хамовнический Вал, 34"
    ADDRESS_B = "Зубовский бульвар, 37"

    @allure.title("Если указать маршрут отображаются две точки на карте ")
    def test_add_route_shows_start_end_points_on_map(self, main_page):
        main_page.type_route(self.ADDRESS_A, self.ADDRESS_B)
        point_a_name = main_page.check_start_address_a_visible()
        point_b_name = main_page.check_start_address_b_visible()
        assert self.ADDRESS_A.lower() in point_a_name.lower(), f"Expected '{self.ADDRESS_A}' to be in '{point_a_name}'"
        assert self.ADDRESS_B.lower() in point_b_name.lower(), f"Expected '{self.ADDRESS_B}' to be in '{point_b_name}'"


    @allure.title("Если указать маршрут отображаются блок с выбором маршрута")
    def test_add_route_shows_block_with_route_selection(self, main_page):
        main_page.type_route(self.ADDRESS_A, self.ADDRESS_B)
        assert main_page.find_visibility_element(MainPageLocators.ROUTE_FORM_PICKER)


    @allure.title("Если указать в маршруте одинаковые адреса отображаются блок с текстом 'Авто Бесплатно В пути 0 мин'")
    def test_add_route_shows_block_with_text_auto_free(self, main_page):
        main_page.type_route(self.ADDRESS_A, self.ADDRESS_A)
        main_page.find_visibility_element(MainPageLocators.TRIP_TOTAL)
        total = main_page.find_visibility_element(MainPageLocators.TRIP_TOTAL).text
        duration = main_page.find_visibility_element(MainPageLocators.TRIP_DURATION).text
        assert total == 'Авто Бесплатно'
        assert duration == "В пути 0 мин."

    @allure.title("При переключении между видами маршрута, происходит смена активного таба и пересчет времени и стоимости маршрута")
    def test_when_switching_between_route_types_active_tab_change_time_and_cost(self, main_page):
        main_page.type_route(self.ADDRESS_A, self.ADDRESS_B)
        first_total = main_page.find_visibility_element(MainPageLocators.TRIP_TOTAL).text
        time.sleep(5)
        main_page.assert_selected_tab(TripMode.OPTIMUM)
        main_page.click_optimal_route()
        second_total = main_page.find_visibility_element(MainPageLocators.TRIP_TOTAL).text
        assert first_total != second_total
        time.sleep(5)
        main_page.assert_selected_tab(TripMode.OPTIMUM)


    @allure.title("При переключении на вид маршрута Свой происходит смена активного таба ,становятся активны типы передвижения")
    def test_when_switching_view_yours(self, main_page):
        main_page.type_route(self.ADDRESS_A, self.ADDRESS_B)
        main_page.click_mine_route()
        main_page.assert_selected_tab(TripMode.OWN)
        main_page.assert_all_trip_types_available()


    @allure.title("При выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_taxi_available_in_fast_mode(self, main_page):
        main_page.type_route(self.ADDRESS_A, self.ADDRESS_B)
        main_page.click_fast_route()

        assert main_page.find_visibility_element(MainPageLocators.TRIP_TOTAL).is_displayed()

    @allure.title("При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать")
    def test_book_button_available_in_own_mode_and_trip_drive(self, main_page):
        main_page.type_route(self.ADDRESS_A, self.ADDRESS_B)
        main_page.click_mine_route()
        main_page.click_type_of_movement_drive()

        assert main_page.find_visibility_element(MainPageLocators.BUTTON_BOOK).is_displayed()

    @allure.title("Форма заказа такси открывается и доступны 6 тарифов, Рабочий тариф активный")
    def test_taxi_order_has_6_tariffs(self, main_page_set_trip):
        main_page_set_trip.assert_all_taxi_types_available()
        main_page_set_trip.assert_taxi_tariff_is_selected(TaxiTariff.WORK)