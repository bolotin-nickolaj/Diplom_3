from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    #Иконка отобразить/скрыть пароль в окне ввода пароля
    PWD_VISIBLE = (By.CLASS_NAME, "input__icon.input__icon-action")

    #Пароль
    VIEW_PWD = (By.XPATH, "//label[text()='Пароль']")

    #Кнопка сохранить
    SAVE_BTT = (By.XPATH, "//button[text()='Сохранить']")