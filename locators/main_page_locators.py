from selenium.webdriver.common.by import By


class MainPageLocators:
    FROM_INPUT = (By.ID, 'from')
    TO_INPUT = (By.ID, 'to')
    LABEL_A = (By.XPATH, "//ymaps[contains(@class,'RouterWayPointSmallLetter0')]")
    LABEL_B = (By.XPATH, "//ymaps[contains(@class,'RouterWayPointSmallLetter1')]")

    LABEL_A_TEXT = (By.XPATH, LABEL_A[1] + "/parent::ymaps/ymaps[3]")
    LABEL_B_TEXT = (By.XPATH, LABEL_B[1] + "/parent::ymaps/ymaps[3]")

    ROUTE_FORM_PICKER = (By.XPATH, "//div[starts-with(@class, 'type-picker')]")
    TRIP_TOTAL = (By.XPATH, "//div[@class='results-text']/div")
    TRIP_DURATION = (By.XPATH, "//div[@class='results-text']/div[2]")

    PICKER_MODE_OPTIMUM = (By.XPATH, "//div[text()='Оптимальный']")
    PICKER_MODE_FAST = (By.XPATH, "//div[text()='Быстрый']")
    PICKER_MODE_OWN = (By.XPATH, "//div[text()='Свой']")


    TRIP_TYPE_CAR = (By.XPATH, "//div[starts-with(@class,'type')]/img[contains(@src, 'media/car')]")
    TRIP_TYPE_WALK = (By.XPATH, "//div[starts-with(@class,'type')]/img[contains(@src, 'media/walk')]")
    TRIP_TYPE_TAXI = (By.XPATH, "//div[starts-with(@class,'type')]/img[contains(@src, 'media/taxi')]")
    TRIP_TYPE_BIKE = (By.XPATH, "//div[starts-with(@class,'type')]/img[contains(@src, 'media/bike')]")
    TRIP_TYPE_SCOOTER = (By.XPATH, "//div[starts-with(@class,'type')]/img[contains(@src, 'media/scooter')]")
    TRIP_TYPE_DRIVE = (By.XPATH, "//div[starts-with(@class,'type')]/img[contains(@src, 'media/drive')]")


    TRIP_TOTAL = (By.XPATH, "//div[@class='results-text']/div")
    TRIP_DURATION = (By.XPATH, "//div[@class='results-text']/div[2]")
    BUTTON_CALL_TAXI = (By.XPATH, "//button[text()='Вызвать такси']")
    BUTTON_BOOK = (By.XPATH, "//button[text()='Забронировать']")

    TAXI_TARIFF_BLOCK = (By.XPATH, "//div[@class='tariff-cards']/div[{}]")
    TAXI_TARIFF_BLOCK_BUTTON = (By.XPATH, TAXI_TARIFF_BLOCK[1] + "/button")
    TAXI_TARIFF_COST_TXT = (By.XPATH, TAXI_TARIFF_BLOCK[1]+"/div[@class='tcard-price']")