import time

import pytest
import allure

#from selenium.common import TimeoutException
import urls
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl
from locators.order_waiting_locators import OrderWaitingLocators as Orl
#from locators.order_window_locators import OrderWindowLocators as Owl


@allure.feature("Заказ такси")
class TestTaxiOrderFlow:
    @allure.story("Полный флоу заказа такси с проверкой окна ожидания")
    @allure.title("Проверка окна ожидания машины после заказа такси")
    def test_taxi_order_waiting_screen(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.prepare_taxi_order()
        main_page.click_element(Fsl.WORKER_TARIFF)
        main_page.click_element(Fsl.REQUIREMENTS_HEADER)
        main_page.click_element(Fsl.LAPTOP_TABLE_SWITCH)
        main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)

        assert main_page.get_element_text(Orl.ORDER_HEADER_TITLE) == "Поиск машины"
        assert main_page.check_is_displayed(Orl.ORDER_TIMER)
        assert main_page.get_element_text(Orl.CANCEL_BUTTON_TEXT) == "Отменить", "Неверный текст кнопки Отменить"
        assert main_page.get_element_text(Orl.DETAILS_BUTTON_TEXT) == "Детали", "Неверный текст кнопки Детали"





