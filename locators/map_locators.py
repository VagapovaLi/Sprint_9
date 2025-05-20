from selenium.webdriver.common.by import By


class MapLocators:

# Точки маршрута
    ROUTE_POINTS = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-route-pin")
    START_POINT = (By.XPATH, "//ymaps[contains(@class, 'route-pin__label-0')]")
    END_POINT = (By.XPATH, "//ymaps[contains(@class, 'route-pin__label-1')]")
