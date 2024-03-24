import allure
from locators.head_page_locators import HeadPageLocators as locators
from pages.base_page import BasePage


class HeadPage(BasePage):

    @allure.step("Нажатие на элемент Личный кабинет")
    def personal_account_located_click(self):
        self.find_presence_of_element_located(locators.PERSONAL_ACCOUNT_REF).click()

    @allure.step("Нажатие на кнопку Конструктор")
    def designer_button_click(self):
        self.find_presence_of_element_located(locators.DESIGNER_REF).click()

    @allure.step("Нажатие на кнопку ленту заказов")
    def orders_feed_button_click(self):
        self.find_presence_of_element_located(locators.ORDER_FEED_REF).click()

    @allure.step("Получение класса элемента Конструктор")
    def get_class_of_designer(self):
        return self.get_attribute_class_of_element(locator=locators.DESIGNER_REF)

    @allure.step("Получение класса элемента Лента заказов")
    def get_class_of_orders_feed(self):
        return self.get_attribute_class_of_element(locator=locators.ORDER_FEED_REF)

    @allure.step("Нажатие на ингредиент")
    def ingredient_click(self):
        self.find_presence_of_element_located(locators.ING_REF).click()

    @allure.step("Получение класса вкладки Лента заказов")
    def get_class_of_ingredient(self):
        return self.get_attribute_class_of_element(locator=locators.ING_WINDOW)

    @allure.step("Закрытие детализации ингридиента")
    def close_ing_det_click(self):
        self.find_presence_of_element_located(locators.ING_DET_CLOSE).click()

    @allure.step("Получение количества ингридиентов")
    def get_count_ingredient(self):
        return self.get_property_textContent_of_element(locator=locators.COUNT_OF_INGREDIENT)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_and_drop(locators.ING_REF, locators.ADD_TO_ORDER)

    @allure.step("Ожидание кнопки Оформить заказ")
    def waiting_make_order_button(self):
        self.wait_control_visibility(locators.MAKE_ORDER)

    @allure.step("Нажатие на кнопку 'Оформить заказ'")
    def make_order_button_press(self):
        self.find_presence_of_element_located(locators.MAKE_ORDER).click()

    @allure.step("Ожидание номера заказа'")
    def waiting_number_of_order(self):
        self.waiting_text_disapear(locators.NUMBER_OF_ORDER, '9999')

    @allure.step("Получение номера заказа")
    def get_order_id(self):
        self.waiting_text_disapear(locators.NUMBER_OF_ORDER, '9999')
        return self.find_visibility_of_element_located(locator=locators.NUMBER_OF_ORDER).text

    @allure.step("Закрытие окна заказа")
    def close_order_window(self):
        self.wait_element(locator=locators.ORDER_WINDOW)
        self.press_on_element(locator=locators.ORDER_WINDOW)