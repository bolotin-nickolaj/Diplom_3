import allure
from locators.login_page_locators import LoginPageLocators
from locators.head_page_locators import HeadPageLocators
from locators.forgot_password_locators import ForgotPasswordLocators
from constant import TestData
from pages.base_page import BasePage
from url import Urls


class LoginPage(BasePage):

    @allure.step("Логин пользователя")
    def user_login(self):
        self.find_presence_of_element_located(LoginPageLocators.INPUT_EMAIL).send_keys(TestData.email)
        self.find_presence_of_element_located(LoginPageLocators.INPUT_PASSWORD).send_keys(TestData.passwd)
        self.find_presence_of_element_located(LoginPageLocators.INPUT_BUTTON).click()
        self.find_presence_of_element_located(HeadPageLocators.PERSONAL_ACCOUNT_REF)

    @allure.step("Ожидание кнопки Вход")
    def wait_input(self):
        self.wait_control_visibility(LoginPageLocators.INPUT_BUTTON)

    @allure.step("Нажатие кнопки Восстановить пароль")
    def recovery_password_click(self):
        self.go_to_page(Urls.login)
        self.find_presence_of_element_located(ForgotPasswordLocators.PWD_RCVR).click()
