import pytest
import allure
import urls
from pages.main_page import MainPage
from locators.form_search_locators import FormSearchLocators as Fsl

@allure.feature("Заказ такси")
class TestTaxiOrder:

    @allure.story("Проверка тарифов")
    @allure.title("Заказа такси с разными адресами")
    @pytest.mark.parametrize("from_address,to_address", [
        ("Хамовнический Вал, 34", "Зубовский бульвар, 37"),
        ("Зубовский бульвар, 37", "Хамовнический Вал, 34")
    ])
    def test_taxi_order_with_different_addresses(self, driver, from_address, to_address):
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

        active_tariffs = main_page.find_elements(Fsl.ACTIVE_TARIFF_CARD)
        assert len(active_tariffs) == 1


    @allure.story("Проверка тарифов")
    @allure.title("Всплывающих подсказок тарифов")
    @pytest.mark.xfail(reason="Перепутаны тултипы тарифов Сонный и Разговорный")
    def test_tariff_popup_tooltips(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.prepare_taxi_order()
        tariffs_with_expected_tooltips = {

            Fsl.WORKER_TARIFF: {
                "icon": Fsl.WORKER_TOOLTIP_ICON,
                "tooltip": Fsl.WORKER_TOOLTIP,
                "title": Fsl.WORKER_TOOLTIP_TITLE,
                "description": Fsl.WORKER_TOOLTIP_PREFIX,
                "title_ex": "Рабочий",
                "description_ex": "Для деловых особ, которых отвлекают"
            },
            Fsl.SLEEPY_TARIFF: {
                "icon": Fsl.SLEEPY_TOOLTIP_ICON,
                "tooltip": Fsl.SLEEPY_TOOLTIP,
                "title": Fsl.SLEEPY_TOOLTIP_TITLE,
                "description": Fsl.SLEEPY_TOOLTIP_PREFIX,
                "title_ex": "Сонный",
                "description_ex": "Для тех, кто не выспался"
            },
            Fsl.VACATION_TARIFF: {
                "icon": Fsl.VACATION_TOOLTIP_ICON,
                "tooltip": Fsl.VACATION_TOOLTIP,
                "title": Fsl.VACATION_TOOLTIP_TITLE,
                "description": Fsl.VACATION_TOOLTIP_PREFIX,
                "title_ex": "Отпускной",
                "description_ex": "Если пришла пора отдохнуть"
            },
            Fsl.TALKATIVE_TARIFF: {
                "icon": Fsl.TALKATIVE_TOOLTIP_ICON,
                "tooltip": Fsl.TALKATIVE_TOOLTIP,
                "title": Fsl.TALKATIVE_TOOLTIP_TITLE,
                "description": Fsl.TALKATIVE_TOOLTIP_PREFIX,
                "title_ex": "Разговорчивый",
                "description_ex": "Если мысли не выходят из головы"
            },
            Fsl.COMFORTING_TARIFF: {
                "icon": Fsl.COMFORTING_TOOLTIP_ICON,
                "tooltip": Fsl.COMFORTING_TOOLTIP,
                "title": Fsl.COMFORTING_TOOLTIP_TITLE,
                "description": Fsl.COMFORTING_TOOLTIP_PREFIX,
                "title_ex": "Утешительный",
                "description_ex": "Если хочется свернуться калачиком"
            },
            Fsl.GLOSSY_TARIFF: {
                "icon": Fsl.GLOSSY_TOOLTIP_ICON,
                "tooltip": Fsl.GLOSSY_TOOLTIP,
                "title": Fsl.GLOSSY_TOOLTIP_TITLE,
                "description": Fsl.GLOSSY_TOOLTIP_PREFIX,
                "title_ex": "Глянцевый",
                "description_ex": "Если нужно блистать"
            }

        }
        for tariff, tooltip in tariffs_with_expected_tooltips.items():
            main_page.click_element(tariff)
            main_page.hover_over_element(tooltip['icon'])
            assert main_page.check_is_displayed(tooltip['tooltip']), "Тултип не отобразился"
            tooltip_data = main_page.get_tooltip_text(tooltip['title'], tooltip['description'])
            assert tooltip["title_ex"] in tooltip_data["title"], "Неверный заголовок тултипа"
            assert tooltip_data["description"] in tooltip["description_ex"], f"Неверное описание тултипа {tooltip['title']}"

    @allure.story("Проверка формы заказа")
    @allure.title("Проверка полей формы заказа такси")
    def test_taxi_order_form_fields(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.SITE_URL)
        main_page.prepare_taxi_order()

        required_fields = {
            "Телефон": Fsl.PHONE_FIELD,
            "Способ оплаты": Fsl.PAYMENT_METHOD,
            "Комментарий": Fsl.COMMENT_FIELD,
            "Требования": Fsl.REQUIREMENTS_SECTION
        }

        for field_name, locator in required_fields.items():
            assert main_page.check_is_displayed(locator), f"Поле {field_name} не отображается"
