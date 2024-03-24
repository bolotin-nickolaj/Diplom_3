from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Карточка заказа
    ORDER_CARD = (By.XPATH, "//a[contains(@class, 'OrderHistory_link__1iNby')]")

    # Отображение карточки заказа
    ORDER_DETAILS_CARD = (By.XPATH, "//section[contains(@class, 'opened__3ISw4')]")

    # Лента заказов
    FEED_OF_ORDERS = (By.XPATH, "//p[@class='text text_type_digits-default']")

    # Количество всех заказов
    ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    # Количество заказов за день
    ORDERS_IN_DAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # Заказы в работе
    ORDERS_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li")

    # Заказы готовы
    ORDERS_READY = (By.XPATH, "//li[contains(@class, 'text text_type_digits-default mb-2')]")
