from selenium.webdriver.common.by import By


class OrderWaitingLocators:
    # Основные элементы
    ORDER_WAITING_CONTAINER = (By.CSS_SELECTOR, ".order-body")
    ORDER_HEADER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    ORDER_TIMER = (By.CSS_SELECTOR, ".order-header-time")
    CANCEL_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]/following-sibling::div")  # "Отменить"
    DETAILS_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]/following-sibling::div")  # "Детали"
    CANCEL_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]")
