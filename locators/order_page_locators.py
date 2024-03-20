from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_CARD = (By.XPATH, "//div[contains(@class, 'OrderFeed_contentBox')]/ul/li[1]")
    ORDER_DETAILS_CARD = (By.XPATH, "//section[2][contains(@class, 'Modal_modal__P3_V5')]")
    FEED_OF_ORDERS = (By.XPATH, "//p[@class='text text_type_digits-default']")
    ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDERS_IN_DAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_READY = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[1]")
    FIRST_OF_ORDERS_FEED = (By.XPATH, "//p[@class='text text_type_digits-default'][1]")
