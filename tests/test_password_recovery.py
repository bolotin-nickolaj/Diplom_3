import time
import allure
from pages.login_page import LoginPage as LP
from pages.forgot_password_page import ForgotPasswordPage as FP
from pages.reset_password_page import ResetPasswordPage as RP
from url import Urls


class TestPasswordRecovery:

    @allure.title("Переход по ссылке Восстановить пароль")
    def test_got_recover_password(self, driver):
        login_page = LP(driver)
        time.sleep(3)
        login_page.recovery_password_click()
        forgot_password_page = FP(driver)
        forgot_password_page.wait_page_load()
        assert forgot_password_page.get_current_page() == Urls.forgot_pwd

    @allure.title("Ввести email и нажать кнопку Восстановить")
    def test_input_email_and_press_recovery_button(self, driver):
        forgot_password_page = FP(driver)
        forgot_password_page.input_email()
        reset_password_page = RP(driver)
        reset_password_page.wait_page_load()
        myUrl = reset_password_page.get_current_page()
        assert myUrl == Urls.reset_pwd

    @allure.title("Нажатие на кнопку показать/скрыть пароль")
    def test_press_button_visible_invisible_password(self, driver):
        forgot_password_page = FP(driver)
        forgot_password_page.input_email()
        reset_password_page = RP(driver)
        reset_password_page.wait_page_load()
        time.sleep(3)
        my_class = reset_password_page.click_visible_pass()
        assert "input__placeholder-focused" in my_class
