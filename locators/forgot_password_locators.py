from selenium.webdriver.common.by import By


class ForgotPasswordLocators:

    # Ссылка Восстановить пароль
    PWD_RCVR = (By.XPATH, "//a[@href='/forgot-password']")

    # Кнопка Восстановить
    PWD_RCVR_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Поле ввода пароля
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
