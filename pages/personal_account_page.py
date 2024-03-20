import allure
from locators.personal_account_locators import PersonalAccountPageLocators as L
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    @allure.step("Нажатие на элемент История заказов")
    def history_order_click(self):
        return self.find_presence_of_element_located(L.ORDERS_HISTORY).click()
    @allure.step("Нажатие на элемент Выход")
    def exit_click(self):
        return self.find_presence_of_element_located(L.EXIT_ON_PERSONAL_ACCOUNT).click()

    @allure.step("Просмотр Ленты заказов")
    def get_orders_history(self):
        return self.find_presence_of_elements_located(L.HISTORY_OF_ORDERS)