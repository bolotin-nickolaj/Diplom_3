import allure
from locators.reset_password_locators import ResetPasswordLocators as locators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step("Ввод email для восстановления пароля")
    def click_visible_pass(self):
        self.find_presence_of_element_located(locator=locators.PWD_VISIBLE).click()
        return self.get_attribute_class_of_element(locator=locators.VIEW_PWD)

    @allure.step("Нажатие на иконку показать/скрыть пароль")
    def show_password_click(self):
        self.find_presence_of_element_located(locator=locators.PWD_VISIBLE).click()

    @allure.step("Ожидание загрузки страницы")
    def wait_page_load(self):
        self.wait_control_visibility(locator=locators.SAVE_BTT)
