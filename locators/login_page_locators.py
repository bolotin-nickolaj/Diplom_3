from selenium.webdriver.common.by import By

class LoginPageLocators:
    #Форма на странице входа и кнопка "Вход"
    INPUT_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button[text()='Войти']")
    #Поля ввода на странице Вход: почта, пароль
    INPUT_EMAIL = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/fieldset[1]/div/div/input")
    INPUT_PASSWORD = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input")
