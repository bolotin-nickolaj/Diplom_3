import allure
from locators.order_page_locators import OrderPageLocators as locators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Нажать на карточку заказа.")
    def order_card_press(self):
        self.find_presence_of_element_located(locator=locators.ORDER_CARD).click()

    @allure.step("Просмотр заказа.")
    def get_class_of_order_card(self):
        return self.get_attribute_class_of_element(locator=locators.ORDER_DETAILS_CARD)

    @allure.step("Просмотр ленты заказов.")
    def get_feed_of_orders(self):
        return self.find_presence_of_elements_located(locator=locators.FEED_OF_ORDERS)

    @allure.step("Количество элементов списка 1 в списке 2")
    def get_count_items_from_list1_into_list2(self, list1, list2):
        count = 0
        for item in list1:
            if item in list2:
                count += 1
        return count

    @allure.step("Возвращает количество всех заказов.")
    def get_count_of_orders(self):
        return self.get_property_textContent_of_element(locator=locators.ORDERS)

    @allure.step("Возвращает количества заказов за день.")
    def get_count_of_orders_in_day(self):
        return self.get_property_textContent_of_element(locator=locators.ORDERS_IN_DAY)

    @allure.step("Получение списка текстов заказов из списка заказов В РАБОТЕ.")
    def get_list_of_orders_inwork_text(self):
        orders = self.find_presence_of_elements_located(locator=locators.ORDERS_WORK)
        return self.get_list_of_elements(orders)

    @allure.step("Ожидание появления № текущего заказа в столбце В работе")
    def wait_order_in_inwork(self, order):
        self.waiting_text(locators.ORDERS_WORK, order)
        return self.find_visibility_of_element_located(locator=locators.ORDERS_WORK).text
