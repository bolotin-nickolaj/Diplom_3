import allure
from locators.order_page_locators import OrderPageLocators as O
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step("Нажать на карточку заказа.")
    def order_card_press(self):
        self.find_presence_of_element_located(O.ORDER_CARD).click()

    @allure.step("Просмотр заказа.")
    def get_class_of_order_card(self):
        return self.find_presence_of_element_located(O.ORDER_DETAILS_CARD).get_attribute('class')

    @allure.step("Просмотр ленты заказов.")
    def get_feed_of_orders(self):
        return self.find_presence_of_elements_located(O.FEED_OF_ORDERS)

    @allure.step("Количество элементов списка 1 в списке 2")
    def get_count_items_from_list1_into_list2(self, list1, list2):
        count = 0
        for item in list1:
            if item in list2:
                count += 1
        return count

    @allure.step("Возвращает количество всех заказов.")
    def get_count_of_orders(self):
        return self.find_presence_of_element_located(O.ORDERS).get_property("textContent")

    @allure.step("Возвращает количества заказов за день.")
    def get_count_of_orders_in_day(self):
        return self.find_presence_of_element_located(O.ORDERS_IN_DAY).get_property("textContent")

    @allure.step("Получение списка текстов заказов из списка заказов.")
    def get_list_of_orders_text(self):
        orders = self.find_presence_of_elements_located(O.ORDERS_READY)
        list = []
        for item in orders:
            list.append(item.text)
        return list
