from selenium.webdriver.common.by import By


class LoginPageLocators:

    #Форма на странице входа и кнопка "Вход"
    INPUT_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button[text()='Войти']")

    #Поля ввода на странице Вход: почта, пароль
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input")
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/../input")
