import time
import allure
from url import Urls
from pages.head_page import HeadPage as H
from pages.login_page import LoginPage as L

class TestHeadPage:

    @allure.title("переход по клику на «Конструктор»")
    def test_designer_click(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        time.sleep(3)
        hp.orders_feed_button_click()
        hp.designer_button_click()
        selected_element_class = hp.get_class_of_designer()
        assert 'link_active' in selected_element_class

    @allure.title("переход по клику на «Лента заказов»")
    def test_orders_feed_click(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        time.sleep(3)
        hp.orders_feed_button_click()
        selected_element_class = hp.get_class_of_orders_feed()
        assert 'link_active' in selected_element_class

    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredien_click(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        time.sleep(3)
        hp.ingredient_click()
        selected_element_class = hp.get_class_of_ingredient()
        assert 'Modal_modal_opened' in selected_element_class

    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_ingredient_window_exit(self, driver):
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        time.sleep(3)
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
        lp = L(driver)
        lp.go_to_page(Urls.login)
        lp.user_login()
        time.sleep(3)
        hp = H(driver)
        hp.go_to_page(Urls.head_page)
        time.sleep(3)
        hp.add_ingredient_to_order()
        hp.make_order_button_press()
        time.sleep(3)
        order_id = hp.get_order_id()
        assert order_id != '9999'



