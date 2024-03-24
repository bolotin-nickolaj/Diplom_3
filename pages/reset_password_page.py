import allure
from locators.reset_password_locators import ResetPasswordLocators as RP
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step("Ввод email для восстановления пароля")
    def click_visible_pass(self):
        self.find_presence_of_element_located(RP.PWD_VISIBLE).click()
        return self.find_presence_of_element_located(RP.VIEW_PWD).get_attribute('class')

    @allure.step("Нажатие на иконку показать/скрыть пароль")
    def show_password_click(self):
        self.find_presence_of_element_located(RP.PWD_VISIBLE).click()

    @allure.step("Ожидание загрузки страницы")
    def wait_page_load(self):
        self.wait_control_visibility(RP.SAVE_BTT)
