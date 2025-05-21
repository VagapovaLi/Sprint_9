import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver, timeout=50):
        self.driver = driver
        self.timeout = timeout


    def find_clickable_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))


    @allure.step('Ищем элемент по {locator} и возвращением его')
    def find_element(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
        return element

    @allure.step('Ждем когда элемент {locator} загрузится')
    def wait_for_load(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за отведенное время.")
            raise

    # Метод ждущий когда элемент станет кликабельным
    @allure.step('Ждем когда элемент {locator} станет кликабельным')
    def wait_for_click(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не стал кликабельным за отведенное время.")
            raise


    def find_elements(self, locator):

        try:
            elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return elements
        except TimeoutException:
            return []


    @allure.step('Открываем страницу {url}')
    def open(self, url):
        self.driver.get(url)


    # Метод для ввода текста, set_data - текст для ввода
    @allure.step('Вводим текст {set_data} в поле ввода {locator}')
    def set_input(self, locator, set_data):
        self.find_clickable_element(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(set_data)

    @allure.step('Проверяем видимость элемента {locator}')
    def check_is_displayed(self, locator):
        try:
            self.wait_for_load(locator)
            is_displayed = self.driver.find_element(*locator).is_displayed()
            return is_displayed
        except TimeoutException:
            return False

    @allure.step('Достаем текст элемента по локатору {locator}')
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Нажимаем на элемент {locator}')
    def click_element(self, locator):
        try:
            self.wait_for_click(locator)
            self.driver.find_element(*locator).click()
        except Exception as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise e


    @allure.step("Навести курсор на элемент")
    def hover_over_element(self, locator):
        """Наводит курсор на указанный элемент"""
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Дождаться исчезновения элемента")
    def wait_for_invisibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator))