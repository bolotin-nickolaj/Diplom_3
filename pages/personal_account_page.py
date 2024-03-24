import allure
from locators.personal_account_locators import PersonalAccountPageLocators as locators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step("Нажатие на элемент История заказов")
    def history_order_click(self):
        return self.find_presence_of_element_located(locator=locators.ORDERS_HISTORY).click()

    @allure.step("Нажатие на элемент Выход")
    def exit_click(self):
        return self.find_presence_of_element_located(locator=locators.EXIT_ON_PERSONAL_ACCOUNT).click()

    @allure.step("Просмотр Ленты заказов")
    def get_orders_history(self):
        return self.find_presence_of_elements_located(locator=locators.HISTORY_OF_ORDERS)
