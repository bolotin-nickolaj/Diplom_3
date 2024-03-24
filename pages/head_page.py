import allure
from locators.head_page_locators import HeadPageLocators as H
from pages.base_page import BasePage


class HeadPage(BasePage):

    @allure.step("Нажатие на элемент Личный кабинет")
    def personal_account_located_click(self):
        self.find_presence_of_element_located(H.PERSONAL_ACCOUNT_REF).click()

    @allure.step("Найти на элемент Личный кабинет")
    def personal_account_click(self, time=20):
        self.find_element_located_click(H.PERSONAL_ACCOUNT_REF, time)

    @allure.step("Нажатие на элемент Личный кабинет")
    def personal_account_clickable_click(self):
        self.find_element_to_be_clickable(H.PERSONAL_ACCOUNT_REF).click()

    @allure.step("Ожидание кнопки Войти в аккаунт")
    def waiting_for_the_login_button(self):
        self.wait_control_visibility(H.LOGIN_ACCOUNT_BUTTON)

    @allure.step("Ожидание ссылки Лента заказов")
    def waiting_for_the_orders_feed_button(self):
        self.wait_control_visibility(H.ORDER_FEED_REF)

    @allure.step("Нажатие на кнопку Конструктор")
    def designer_button_click(self):
        self.find_presence_of_element_located(H.DESIGNER_REF).click()

    @allure.step("Нажатие на кнопку ленту заказов")
    def orders_feed_button_click(self):
        self.find_presence_of_element_located(H.ORDER_FEED_REF).click()

    @allure.step("Получение класса элемента Конструктор")
    def get_class_of_designer(self):
        return self.get_attribute_class_of_element(locator=H.DESIGNER_REF)

    @allure.step("Получение класса элемента Лента заказов")
    def get_class_of_orders_feed(self):
        return self.get_attribute_class_of_element(locator=H.ORDER_FEED_REF)

    @allure.step("Нажатие на ингредиент")
    def ingredient_click(self):
        self.find_presence_of_element_located(H.ING_REF).click()

    @allure.step("Получение класса вкладки Лента заказов")
    def get_class_of_ingredient(self):
        return self.get_attribute_class_of_element(locator=H.ING_WINDOW)

    @allure.step("Закрытие детализации ингридиента")
    def close_ing_det_click(self):
        self.find_presence_of_element_located(H.ING_DET_CLOSE).click()

    @allure.step("Получение количества ингридиентов")
    def get_count_ingredient(self):
        return self.get_property_textContent_of_element(locator=H.COUNT_OF_INGREDIENT)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_and_drop(H.ING_REF, H.ADD_TO_ORDER)

    @allure.step("Ожидание кнопки Оформить заказ")
    def waiting_make_order_button(self):
        self.wait_control_visibility(H.MAKE_ORDER)

    @allure.step("Нажатие на кнопку 'Оформить заказ'")
    def make_order_button_press(self):
        self.find_presence_of_element_located(H.MAKE_ORDER).click()

    @allure.step("Ожидание номера заказа'")
    def waiting_number_of_order(self):
        self.waiting_text_disapear(H.NUMBER_OF_ORDER, '9999')

    @allure.step("Получение номера заказа")
    def get_order_id(self):
        self.waiting_text_disapear(H.NUMBER_OF_ORDER, '9999')
        return self.find_visibility_of_element_located(locator=H.NUMBER_OF_ORDER).text

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        self.wait_element(locator=H.ORDER_WINDOW)
        self.press_on_element(locator=H.ORDER_WINDOW)