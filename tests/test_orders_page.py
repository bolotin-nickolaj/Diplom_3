import allure
from url import Urls
from pages.order_page import OrderPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.head_page import HeadPage

class TestOrderPage:

    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_order_press_popup_window_with_details_will_be_open(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_page(Urls.feed)
        order_page.order_card_press()
        my_class = order_page.get_class_of_order_card()
        assert 'modal_opened' in my_class

    @allure.title("заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов'")
    def test_user_orders_shows_on_orders_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_page(Urls.login)
        login_page.user_login()
        head_page = HeadPage(driver)
        head_page.waiting_make_order_button()
        head_page.personal_account_located_click()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.history_order_click()
        orders_in_history = personal_account_page.get_orders_history()
        list_of_orders_in_history = personal_account_page.get_list_of_elements(orders_in_history)
        order_page = OrderPage(driver)
        order_page.go_to_page(Urls.feed)
        orders_in_feed = order_page.get_feed_of_orders()
        list_of_orders_in_feed = order_page.get_list_of_elements(orders_in_feed)
        my_count = order_page.get_count_items_from_list1_into_list2(list_of_orders_in_history, list_of_orders_in_feed)
        assert my_count > 0

    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_after_creating_new_order_total_counter_increases(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_page(Urls.feed)
        count_before = order_page.get_count_of_orders()
        login_page = LoginPage(driver)
        login_page.go_to_page(Urls.login)
        login_page.user_login()
        head_page = HeadPage(driver)
        head_page.waiting_make_order_button()
        head_page.add_ingredient_to_order()
        head_page.make_order_button_press()
        order_page.go_to_page(Urls.feed)
        count_after = order_page.get_count_of_orders()

        assert int(count_after) == int(count_before) + 1

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_after_creating_new_order_day_counter_increases(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_page(Urls.feed)
        count_before = order_page.get_count_of_orders_in_day()
        login_page = LoginPage(driver)
        login_page.go_to_page(Urls.login)
        login_page.user_login()
        head_page = HeadPage(driver)
        head_page.waiting_make_order_button()
        head_page.add_ingredient_to_order()
        head_page.make_order_button_press()
        order_page.go_to_page(Urls.feed)
        count_after = order_page.get_count_of_orders_in_day()
        assert int(count_after) == int(count_before) + 1

    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_after_creating_new_order_its_number_appears_in_work_section(self, driver):
        order_page = OrderPage(driver)
        login_page = LoginPage(driver)
        login_page.go_to_page(Urls.login)
        login_page.user_login()
        head_page = HeadPage(driver)
        head_page.waiting_make_order_button()
        head_page.add_ingredient_to_order()
        head_page.make_order_button_press()
        head_page.waiting_number_of_order()
        order_id = head_page.get_order_id()
        head_page.close_order_window()
        order_page.go_to_page(Urls.feed)
        order_id = "0" + order_id
        order_page.wait_order_in_inwork(order_id)
        texts = order_page.get_list_of_orders_inwork_text()
        assert order_id in texts
