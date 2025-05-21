import pytest
import allure


import urls
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl
from locators.order_waiting_locators import OrderWaitingLocators as Orl

from locators.order_window_locators import OrderWindowLocators as Owl


@allure.feature("Заказ такси")
class TestTaxiOrderFlow:
    @allure.story("Полный путь заказа такси с проверкой окна ожидания")
    @allure.title("Проверка окна ожидания машины после заказа такси")
    def test_waiting_window_taxi_order(self, driver):
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



    @allure.story("Полный путь заказа такси с проверкой окна завершенного заказа после поиска машины")
    @allure.title("Отображение элементов окна найденной машины")
    def test_display_element_the_window_found_machine(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.prepare_taxi_order()
        main_page.click_element(Fsl.WORKER_TARIFF)
        main_page.click_element(Fsl.REQUIREMENTS_HEADER)
        main_page.click_element(Fsl.LAPTOP_TABLE_SWITCH)
        main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)
        main_page.wait_for_invisibility(Orl.ORDER_TIMER, 120)

        assert main_page.check_is_displayed(Owl.ORDER_HEADER), "Заголовок не отображается"
        assert main_page.check_is_displayed(Owl.CAR_NUMBER), "Номер машины не отображается"
        assert main_page.check_is_displayed(Owl.CAR_ICON), "Информация о водителе не отображается"

        assert main_page.check_is_displayed(Owl.DRIVER_RATING), "Рейтинг водителя не отображается"
        assert main_page.check_is_displayed(Owl.DRIVER_NAME), "Имя водителя не отображается"
        assert main_page.check_is_displayed(Owl.DRIVER_AVATAR), "Аватарка водителя не отображается"

        assert main_page.check_is_displayed(Owl.CANCEL_BUTTON), "Кнопка отмены не отображается"
        assert main_page.check_is_displayed(Owl.DETAILS_BUTTON), "Кнопка детали не отображается"


    @allure.story("Проверка стоимости в деталях заказа")
    @allure.title("Сравнение стоимости в деталях с выбранным тарифом")
    def test_price_in_order_details(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.prepare_taxi_order()

        main_page.click_element(Fsl.WORKER_TARIFF)
        initial_price = main_page.get_element_text(Fsl.WORKER_TARIFF_PRICE)
        main_page.click_element(Fsl.REQUIREMENTS_HEADER)
        main_page.click_element(Fsl.LAPTOP_TABLE_SWITCH)
        main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)

        main_page.wait_for_invisibility(Orl.ORDER_TIMER, 120)

        main_page.click_element(Owl.DETAILS_BUTTON)
        price_in_details = main_page.get_element_text(Owl.ORDER_PRICE)

        normalized_initial_price = main_page.normalize_price(initial_price)
        normalized_price_in_details = main_page.normalize_price(price_in_details)

        assert normalized_initial_price == normalized_price_in_details, \
            f"Стоимость не совпадает. Ожидалось: {initial_price}, Фактически: {price_in_details}"


    @allure.story("Отмена заказа через кнопку 'Отменить'")
    @allure.title("Закрытия окна после отмены заказа")
    @pytest.mark.xfail(reason="Модальное окно заказа, не закрывается по нажатию на кнопку Отмены")
    def test_cancel_order_closes_window(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.prepare_taxi_order()

        main_page.click_element(Fsl.WORKER_TARIFF)
        main_page.click_element(Fsl.REQUIREMENTS_HEADER)
        main_page.click_element(Fsl.CONFIRM_ORDER_BUTTON)
        main_page.click_element(Orl.CANCEL_BUTTON)
        main_page.wait_for_invisibility(Orl.ORDER_WAITING_CONTAINER, 10)
        assert not main_page.check_is_displayed(Orl.ORDER_WAITING_CONTAINER), \
            "Окно заказа все еще отображается после отмены"