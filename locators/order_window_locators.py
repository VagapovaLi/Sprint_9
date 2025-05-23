from selenium.webdriver.common.by import By


class OrderWindowLocators:

    ORDER_HEADER = (By.CSS_SELECTOR, ".order-header")
    CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")  # "п 367 уг"
    CAR_ICON = (By.CSS_SELECTOR, ".order-number img[alt='Car']")
    DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")  # "4,9"
    DRIVER_NAME = (By.XPATH,
                   "//div[contains(@class, 'order-btn-group') and .//div[contains(@class, 'order-btn-rating')]]/following-sibling::div")  # "Жубан"
    DRIVER_AVATAR = (By.CSS_SELECTOR, "img[alt='close']")
    CANCEL_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]")
    CANCEL_BUTTON_TEXT = (By.XPATH, "//button[.//img[contains(@src, 'plus')]]/following-sibling::div")  # "Отменить"

    DETAILS_BUTTON = (By.XPATH, "//button[.//img[contains(@src, 'burger')]]")

    # Стоимость
    ORDER_PRICE = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Стоимость')]")