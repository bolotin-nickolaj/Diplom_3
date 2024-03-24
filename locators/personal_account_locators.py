from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    #Ссылка на "Историю заказов"
    ORDERS_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")

    #Кнопка "Выход" на странице "Личный кабинет"
    EXIT_ON_PERSONAL_ACCOUNT = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")

    # Ссылка на "Ленту заказов"
    ORDER_FEED = (By.XPATH, "//a[@href='/feed']")

    # Ссылка на историю заказов
    HISTORY_OF_ORDERS = (By.XPATH, "//p[@class='text text_type_digits-default']")
