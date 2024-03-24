import allure
from locators.forgot_password_locators import ForgotPasswordLocators as FP
from pages.base_page import BasePage
from constant import TestData
from url import Urls

class ForgotPasswordPage(BasePage):

    @allure.step("Ввод email для восстановления пароля")
    def input_email(self):
        self.go_to_page(Urls.forgot_pwd)
        self.wait_page_load()
        self.find_presence_of_element_located(FP.EMAIL).send_keys(TestData.email)
        self.find_presence_of_element_located(FP.PWD_RCVR_BUTTON).click()

    @allure.step("Ожидание загрузки страницы")
    def wait_page_load(self):
        self.wait_control_visibility(FP.EMAIL)
