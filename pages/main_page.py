import time
import allure

from pages.base_page import BasePage
from locators.form_search_locators import FormSearchLocators as Fsl

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаем на 'Оптимальный' маршрут")
    def click_optimal_route(self):
        self.find_clickable_element(Fsl.MODE_OPTIMAL).click()


    @allure.step("Нажимаем на 'Быстрый' маршрут")
    def click_fast_route(self):
        self.find_clickable_element(Fsl.MODE_FAST).click()

    @allure.step("Нажимаем на 'Вызвать такси' маршрут")
    def click_button_call_taxi(self):
        self.find_clickable_element(Fsl.BUTTON_CALL_TAXI).click()

    @allure.step('Проверяем активность таба тарифа')
    def is_tab_active_route(self, locator):
        tab = self.find_element(locator)
        return "active" in tab.get_attribute("class")

    @allure.step("Нажимаем на 'Свой' маршрут")
    def click_mine_route(self):
        self.find_clickable_element(Fsl.MODE_CUSTOM).click()


    @allure.step("Нажимаем на типа передвижения 'Драйв'")
    def click_type_of_movement_drive(self):
        self.find_clickable_element(Fsl.TRANSPORT_DRIVE).click()

    @allure.step("Нажимаем 'Забронировать' в Драв")
    def click_book_drive(self):
        self.find_clickable_element(Fsl.BUTTON_RESERVATION_DRIVE).click()

    @allure.step("Подготовить заказ такси (ввод адресов и открытие формы)")
    def prepare_taxi_order(self, from_address="Хамовнический Вал, 34", to_address="Зубовский бульвар, 37"):
        self.set_input(Fsl.INPUT_FROM_ADDRESS, from_address)
        self.set_input(Fsl.INPUT_TO_ADDRESS, to_address)
        self.click_fast_route()
        self.click_button_call_taxi()



    @allure.step("Получить текст тултипа")
    def get_tooltip_text(self, title, description):
        return {
            "title": self.get_element_text(title),
            "description": self.get_element_text(description)
        }