import allure
from url import Urls
from pages.head_page import HeadPage as H
from pages.login_page import LoginPage as L
from pages.order_page import OrderPage as O

class TestHeadPage:

    @allure.title("переход по клику на «Конструктор»")
    def test_designer_click(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.orders_feed_button_click()
        hp.designer_button_click()
        selected_element_class = hp.get_class_of_designer()
        assert 'link_active' in selected_element_class

    @allure.title("переход по клику на «Лента заказов»")
    def test_orders_feed_click(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.orders_feed_button_click()
        selected_element_class = hp.get_class_of_orders_feed()
        assert 'link_active' in selected_element_class

    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredien_click(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.ingredient_click()
        selected_element_class = hp.get_class_of_ingredient()
        assert 'Modal_modal_opened' in selected_element_class

    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_ingredient_window_exit(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.ingredient_click()
        hp.close_ing_det_click()
        selected_element_class = hp.get_class_of_ingredient()
        assert 'Modal_modal_opened' not in selected_element_class

    @allure.title("при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_when_ing_added_then_counter_increases(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        hp.add_ingredient_to_order()
        new_ing_count = hp.get_count_ingredient()
        assert int(new_ing_count) == 2

    @allure.title("залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_make_order(self, driver):
        op = O(driver)
        op.go_to_page(Urls.feed)
        count_orders_in_day_before = op.get_count_of_orders_in_day()
        lp = L(driver)
        lp.go_to_page(Urls.login)
        lp.user_login()
        hp = H(driver)
        hp.add_ingredient_to_order()
        hp.waiting_make_order_button()
        hp.make_order_button_press()
        hp.close_order_window()
        op.go_to_page(Urls.feed)
        count_orders_in_day_after = op.get_count_of_orders_in_day()

        assert int(count_orders_in_day_after) - int(count_orders_in_day_before) == 1



