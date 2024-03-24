import time
import allure
from pages.head_page import HeadPage as HP
from pages.personal_account_page import PersonalAccountPage as PA
from pages.login_page import LoginPage as LP
from url import Urls


class TestPersonalAccount:

    @allure.title("Вход по клику на Личный кабинет")
    def test_personal_account_click(self, driver):
        head_page = HP(driver)
        head_page.go_to_page(Urls.head_page)
        time.sleep(3)
        head_page.personal_account_located_click()
        login_page = LP(driver)
        url = login_page.get_current_page()
        assert url == Urls.login

    @allure.title("Переход по клику на История заказов")
    def test_orders_history_click(self, driver):
        login_page = LP(driver)
        login_page.go_to_page(Urls.login)
        login_page.user_login()
        head_page = HP(driver)
        head_page.personal_account_located_click()
        pa_page = PA(driver)
        time.sleep(3)
        pa_page.history_order_click()
        url = pa_page.get_current_page()
        assert url == Urls.order_history

    @allure.title("Выход по клику на Выход")
    def test_exit_from_personal_account(self, driver):
        login_page = LP(driver)
        login_page.go_to_page(Urls.login)
        login_page.user_login()
        head_page = HP(driver)
        time.sleep(3)
        head_page.personal_account_located_click()
        pa_page = PA(driver)
        time.sleep(3)
        pa_page.exit_click()
        login_page.wait_input()
        url = pa_page.get_current_page()
        assert url == Urls.login
