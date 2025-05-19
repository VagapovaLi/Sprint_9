import time
import allure


from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from utils.taxi_tariff import TaxiTariff
from utils.trip_type import TripType
from utils.trip_mode import TripMode

class MainPage(BasePage):

    @allure.step("Выбрать маршруты от {address_from} до {address_to}")
    def type_route(self, address_from, address_to):
        self.find_visibility_element(MainPageLocators.FROM_INPUT).send_keys(address_from)
        self.find_visibility_element(MainPageLocators.TO_INPUT).send_keys(address_to)


    def check_start_address_a_visible(self):
        self.find_visibility_element(MainPageLocators.LABEL_A)
        return self.find_visibility_element(MainPageLocators.LABEL_A_TEXT).text

    def check_start_address_b_visible(self):
        self.find_visibility_element(MainPageLocators.LABEL_B)
        return self.find_visibility_element(MainPageLocators.LABEL_B_TEXT).text

    @allure.step("Нажимаем на 'Оптимальный' маршрут")
    def click_optimal_route(self):
        self.find_clickable_element(MainPageLocators.PICKER_MODE_OPTIMUM).click()


    @allure.step("Нажимаем на 'Быстрый' маршрут")
    def click_fast_route(self):
        self.find_clickable_element(MainPageLocators.PICKER_MODE_FAST).click()


    @staticmethod
    def get_tab_locator(mode):
        if mode == TripMode.OPTIMUM:
            return MainPageLocators.PICKER_MODE_OPTIMUM
        elif mode == TripMode.FAST:
            return MainPageLocators.PICKER_MODE_FAST
        elif mode == TripMode.OWN:
            return MainPageLocators.PICKER_MODE_OWN

    def assert_selected_tab(self, mode):
        tab = MainPage.get_tab_locator(mode)
        time.sleep(5)
        css_class = self.find_visibility_element(tab).get_attribute("class")
        assert "active" in css_class

    @allure.step("Нажимаем на 'Свой' маршрут")
    def click_mine_route(self):
        self.find_clickable_element(MainPageLocators.PICKER_MODE_OWN).click()


    def get_trip_type(self, trip_type):
        if trip_type == TripType.CAR:
            return MainPageLocators.TRIP_TYPE_CAR
        elif trip_type == TripType.WALK:
            return MainPageLocators.TRIP_TYPE_WALK
        elif trip_type == TripType.TAXI:
            return MainPageLocators.TRIP_TYPE_TAXI
        elif trip_type == TripType.BIKE:
            return MainPageLocators.TRIP_TYPE_BIKE
        elif trip_type == TripType.SCOOTER:
            return MainPageLocators.TRIP_TYPE_SCOOTER
        elif trip_type == TripType.DRIVE:
            return MainPageLocators.TRIP_TYPE_DRIVE

    def trip_type_is_available(self, trip_type):
        css_class = self.find_visibility_element(self.get_trip_type(trip_type)).get_attribute("class")
        assert "disable" not in css_class


    @allure.step("Проверяем, что в табе 'Свой' доступны все типы движения на маршруте")
    def assert_all_trip_types_available(self):
        self.trip_type_is_available(TripType.CAR)
        self.trip_type_is_available(TripType.WALK)
        self.trip_type_is_available(TripType.TAXI)
        self.trip_type_is_available(TripType.BIKE)
        self.trip_type_is_available(TripType.SCOOTER)
        self.trip_type_is_available(TripType.DRIVE)


    @allure.step("Нажимаем на типа передвижения 'Драйв'")
    def click_type_of_movement_drive(self):
        self.find_clickable_element(MainPageLocators.TRIP_TYPE_DRIVE).click()


    @allure.step("Нажать вызвать такси")
    def click_button_call_taxi(self):
        self.find_visibility_element(MainPageLocators.BUTTON_CALL_TAXI).click()


    @allure.step("Проверяем, что все типы такси доступны для заказа")
    def assert_all_taxi_types_available(self):
        self.find_visibility_element(self.format_locator(MainPageLocators.TAXI_TARIFF_BLOCK, TaxiTariff.WORK.value))
        self.find_visibility_element(self.format_locator(MainPageLocators.TAXI_TARIFF_BLOCK, TaxiTariff.TALKING.value))
        self.find_visibility_element(self.format_locator(MainPageLocators.TAXI_TARIFF_BLOCK, TaxiTariff.SLEEPY.value))
        self.find_visibility_element(self.format_locator(MainPageLocators.TAXI_TARIFF_BLOCK, TaxiTariff.GLOSSY.value))
        self.find_visibility_element(self.format_locator(MainPageLocators.TAXI_TARIFF_BLOCK, TaxiTariff.COMFORTING.value))
        self.find_visibility_element(self.format_locator(MainPageLocators.TAXI_TARIFF_BLOCK, TaxiTariff.HOLIDAY.value))

    @allure.step("Проверяем")
    def assert_taxi_tariff_is_selected(self, taxi_tariff):
        css_class = (self.find_visibility_element(
            self.format_locator(MainPageLocators.TAXI_TARIFF_BLOCK_BUTTON, taxi_tariff.value)).get_attribute("class"))
        assert "active" in css_class