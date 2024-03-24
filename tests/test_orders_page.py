import time

import allure
from url import Urls
from pages.order_page import OrderPage as O
from pages.login_page import LoginPage as L
from pages.personal_account_page import PersonalAccountPage as P
from pages.head_page import HeadPage as H

class TestOrderPage:

    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_press_popup_window_with_details_will_be_open(self, driver):
        op = O(driver)
        op.go_to_page(Urls.feed)
        op.order_card_press()
        my_class = op.get_class_of_order_card()
        assert 'modal_opened' in my_class

    @allure.title("заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов'")
    def test_user_orders_shows_on_orders_feed(self, driver):
        lp = L(driver)
        lp.go_to_page(Urls.login)
        lp.user_login()
        hp = H(driver)
        hp.waiting_make_order_button()
        time.sleep(3)
        hp.personal_account_located_click()
        pa = P(driver)
        time.sleep(3)
        pa.history_order_click()
        orders_in_history = pa.get_orders_history()
        list_of_orders_in_history = pa.get_list_of_elements(orders_in_history)
        op = O(driver)
        op.go_to_page(Urls.feed)
        orders_in_feed = op.get_feed_of_orders()
        list_of_orders_in_feed = op.get_list_of_elements(orders_in_feed)
        my_count = op.get_count_items_from_list1_into_list2(list_of_orders_in_history, list_of_orders_in_feed)
        assert my_count > 0

    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_after_creating_new_order_total_counter_increases(self, driver):
        op = O(driver)
        op.go_to_page(Urls.feed)
        count_before = op.get_count_of_orders()
        lp = L(driver)
        lp.go_to_page(Urls.login)
        lp.user_login()
        time.sleep(3)
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.waiting_make_order_button()
        time.sleep(3)
        hp.add_ingredient_to_order()
        hp.make_order_button_press()
        time.sleep(3)
        op.go_to_page(Urls.feed)
        count_after = op.get_count_of_orders()

        assert int(count_after) == int(count_before) + 1

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_after_creating_new_order_day_counter_increases(self, driver):
        op = O(driver)
        op.go_to_page(Urls.feed)
        count_before = op.get_count_of_orders_in_day()
        lp = L(driver)
        lp.go_to_page(Urls.login)
        lp.user_login()
        time.sleep(3)
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.waiting_make_order_button()
        time.sleep(3)
        hp.add_ingredient_to_order()
        hp.make_order_button_press()
        time.sleep(3)
        op.go_to_page(Urls.feed)
        count_after = op.get_count_of_orders_in_day()

        assert int(count_after) == int(count_before) + 1

    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_after_creating_new_order_its_number_appears_in_work_section(self, driver):
        lp = L(driver)
        lp.go_to_page(Urls.login)
        lp.user_login()
        time.sleep(3)
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.waiting_make_order_button()
        time.sleep(3)
        hp.add_ingredient_to_order()
        hp.make_order_button_press()
        time.sleep(3)
        order_id = hp.get_order_id()
        order_id = "0" + order_id
        op = O(driver)
        op.go_to_page(Urls.feed)
        time.sleep(3)
        texts = op.get_list_of_orders_text()

        assert order_id in texts
