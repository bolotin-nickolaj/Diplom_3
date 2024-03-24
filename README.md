# Diplom_3
 Тестирование веб-приложения Stellar Burgers. (https://stellarburgers.nomoreparties.site/)

В файле test_head_page.py содержатся тесты для проверки главной страницы:

|#|Наименование теста| Описание теста   |
|--:|:-----|:-----------------|
|1|test_designer_click|переход по клику на «Конструктор»|
|2|test_orders_feed_click|переход по клику на «Лента заказов»|
|3|test_ingredien_click|если кликнуть на ингредиент, появится всплывающее окно с деталями|
|4|test_ingredient_window_exit|всплывающее окно закрывается кликом по крестику|
|5|test_when_ing_added_then_counter_increases|при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается|
|6|test_authorized_user_can_make_order|залогиненный пользователь может оформить заказ|

В файле test_orders_page.py содержатся тесты для проверки заказов:

| # |Наименование теста| Описание теста   |
|--:|:-----|:-----------------|
| 1 |test_order_press_popup_window_with_details_will_be_open|если кликнуть на заказ, откроется всплывающее окно с деталями|
| 2 |test_user_orders_shows_on_orders_feed|заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента заказов'|
| 3 |test_after_creating_new_order_total_counter_increases|при создании нового заказа счётчик Выполнено за всё время увеличивается|
| 4 |test_after_creating_new_order_day_counter_increases|при создании нового заказа счётчик Выполнено за сегодня увеличивается|
| 5 |test_after_creating_new_order_its_number_appears_in_work_section|после оформления заказа его номер появляется в разделе В работ|

В файле test_password_recovery.py содержатся тесты для проверки восстановления пароля:

|#|Наименование теста| Описание теста   |
|--:|:-----|:-----------------|
|1|test_got_recover_password|Переход по ссылке Восстановить пароль|
|1|test_input_email_and_press_recovery_button|Ввести email и нажать кнопку Восстановить|
|1|test_press_button_visible_invisible_password|Нажатие на кнопку показать/скрыть пароль|

В файле test_personal_account.py содержатся тесты для проверки личного кабинета:

|#|Наименование теста| Описание теста   |
|--:|:-----|:-----------------|
|1|test_personal_account_click|Вход по клику на Личный кабинет|
|1|test_orders_history_click|Переход по клику на История заказов|
|1|test_exit_from_personal_account|Выход по клику на Выход|

