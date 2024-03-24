import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Главная страница")
    def go_to_page(self, url):
        return self.driver.get(url)

    @allure.step("Найти элемент")
    def find_presence_of_element_located(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Element not found in {locator}')

    @allure.step("Найти элемент")
    def find_visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=locator), message=f'Element not found in {locator}')

    @allure.step("Дождаться элемента")
    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=locator))

    @allure.step("Нажать на элемент")
    def press_on_element(self, locator):
        self.wait_element(locator)
        self.find_presence_of_element_located(locator).click()

    @allure.step("Найти элемент")
    def find_presence_of_elements_located(self, locator, time=3):
        return (WebDriverWait(self.driver, time)
                .until(EC.presence_of_all_elements_located(locator), message=f'Elements not found in {locator}'))

    @allure.step("Найти элемент")
    def find_element_to_be_clickable(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Element not found in {locator}')

    @allure.step("Найти элемент и нажать на него")
    def find_element_located_click(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Element not found in {locator}').click()

    @allure.step("Вернуть текущую страницу")
    def get_current_page(self):
        return self.driver.current_url

    @allure.step("Элемент виден")
    def wait_control_visibility(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator), message=f'Element not found in {locator}')

    @allure.step("Перенести элемент.")
    def drag_and_drop(self, locator_element, locator_destination):
        source = self.find_element_to_be_clickable(locator_element)
        target = self.find_presence_of_element_located(locator_destination)
        action_chains = ActionChains(self.driver)
        return action_chains.drag_and_drop(source, target).perform()

    @allure.step("Ожидание исчезновения текста.")
    def waiting_text_disapear(self, locator, text):
        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Ожидание появления текста")
    def waiting_text(self, locator, text):
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Получить список элементов.")
    def get_list_of_elements(self, list_element):
        list = []
        for item in list_element:
            list.append(item.text)
        return list

    @allure.step("Получить свойство textContent")
    def get_property_textContent_of_element(self, locator):
        return self.find_presence_of_element_located(locator).get_property("textContent")

    @allure.step("Получить атрибут элемента class")
    def get_attribute_class_of_element(self, locator):
        return self.find_presence_of_element_located(locator).get_attribute("class")