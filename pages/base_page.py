import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver, timeout=50):
        self.driver = driver
        self.timeout = timeout


    def find_visibility_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))


    def find_clickable_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def format_locator(self, locator, text):
        new_locator = (locator[0], locator[1].format(text))
        return new_locator

