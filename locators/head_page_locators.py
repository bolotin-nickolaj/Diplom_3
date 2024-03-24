from selenium.webdriver.common.by import By


class HeadPageLocators:

    #Ссылка на "Личный кабинет"
    PERSONAL_ACCOUNT_REF = (By.XPATH, "//a[@href='/account']")

    #Кнопка "Войти в аккаунт" на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    #Ссылка "Конструктор" из "Личного кабинета"
    DESIGNER_REF = (By.XPATH, "//a[@href='/']")

    #Ссылка "Лента заказов" из "Личного кабинета"
    ORDER_FEED_REF = (By.XPATH, "//a[@href='/feed']")

    #Ссылка на ингредиент Флюоресцентная булка R2-D3
    ING_REF = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    ING_REF2 = (By.XPATH, "//img[@alt='Краторная булка N-200i']/parent::a")

    #Ссылка на модальное окно с описанием ингредиента
    ING_WINDOW = (By.XPATH, "//section[1][contains(@class, 'Modal_modal')]")

    #Ссылка на закрытие "крестик" формы детализации ингридиента
    ING_DET_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")

    #Количество единиц данного ингредиента
    COUNT_OF_INGREDIENT = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div/p")

    #Добавление в заказ
    ADD_TO_ORDER = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket__list')]")
    ADD_TO_ORDER2 = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
    ADD_TO_ORDER3 = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")

    #Оформить заказ
    MAKE_ORDER2 = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    MAKE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")

    #Номер заказа
    NUMBER_OF_ORDER = (By.XPATH, "//div/h2[text()='9999']")

    #Идентификатор заказа
    IDENT_OF_ORDER = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")

