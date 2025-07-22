from selenium.webdriver.common.by import By

class Locators:

    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # кнопка "Личный кабинет"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ"
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Пароль']")  # поле для ввода пароля
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # поле для ввода email на странице входа
    SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]/parent::div')  # Кнопка "Соусы"
    BUN_BUTTON = (By.XPATH, '//span[text()="Булки"]/parent::div')  # кнопка "Булки"
    FILLING_BUTTON = (By.XPATH, '//span[text()="Начинки"]/parent::div')  # Кнопка "Начинка"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться" на странице регистрации
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выход" в личном кабинете
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']//parent::*/input[@type='text' and @name='name']") # поле для ввода имени
    AUTH = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # логотип сайта
    LOGIN_TEXT = (By.XPATH, "//h2[text()='Вход']") # текст "Вход" на странице входа
    LOGIN_BUTTON_ANY_FORMS = (By.XPATH, "//button[contains(text(), 'Войти')]") # кнопка "Войти" на странице входа
    LOGIN_TEXT_WITH_HREF = (By.XPATH, "//a[text()='Войти']")  # текст "Войти" со ссылкой на страницу входа на странице восстановления пароля
    ELEMENT_WITH_LOGIN_TEXT = (By.XPATH, "//*[text() = 'Вход']") # элемент с текстом "Вход" на странице входа
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]") # сообщение об ошибке на странице регистрации
    ERROR_MESSAGE_TWO = (By.XPATH, "//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']") # сообщение об ошибке на странице регистрации (альтернативное) # кнопка "Войти" на странице регистрации, которая ведет на страницу входа
    INFO_MESSAGE = (By.XPATH, "//p[contains(text(),'персональные данные')]") # сообщение о том, что нужно заполнить персональные данные
    HISTORY_SHOP_BUTTON = (By.XPATH, "//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']") # кнопка "История заказов" в личном кабинете