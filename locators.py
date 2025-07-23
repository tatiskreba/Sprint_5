from selenium.webdriver.common.by import By

class Locators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # логотип сайта

    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # кнопка "Личный кабинет"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ"
    EMAIL_FIELD = (By.XPATH, '//div[label[contains(text(),"Email")]]//input')  # поле для ввода email
    NAME_FIELD = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")  # поле для ввода имени
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']") # поле для ввода пароля
    PASSWORD_ERROR = [By.XPATH, '//p[@class="input__error text_type_main-default"]']  # сообщение "Некорректный пароль"

    SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]')  # Кнопка "Соусы"
    BUN_BUTTON = (By.XPATH, '//div[.//span[text()="Булки"]]') # кнопка "Булки"
    FILLING_BUTTON = (By.XPATH, '//span[text()="Начинки"]')  # Кнопка "Начинка"
    ACTIV_TAB = [By.XPATH, '//div[contains(@class, "tab_tab_type_current")]']  # активный раздел
    SAUCES = [By.XPATH, '//h2[text()="Соусы"]/following-sibling::ul[1]']  # выбор соусов
    BUN = [By.XPATH, '//h2[text()="Булки"]/following-sibling::ul[1]']  # выбор булок
    FILLING = [By.XPATH, '//h2[text()="Начинки"]/following-sibling::ul[1]']  # выбор начинок
    CONSTRUCTOR_CONT = [By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]']

    REGISTER_BUTTON = (By.XPATH, '//a[text()="Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    REGISTRATION_BTN = [By.XPATH, '//button[text()="Зарегистрироваться"]']  # кнопка "Зарегистрироваться"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выход" в личном кабинете
    AUTH = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт"
    LOGIN_TEXT_WITH_HREF = (By.XPATH, "//a[text()='Войти']")  # текст "Войти" со ссылкой на страницу входа
    LOGIN_BUTTON_ANY_FORMS = (By.XPATH, "//button[text()='Войти']") # кнопка "Войти" на странице входа
    FORG_PASS_BTN = [By.XPATH, '//a[text()="Восстановить пароль"]']  # кнопка "Восстановить пароль"
    FORM_LOGIN_TEXT = [By.XPATH, '//a[text()="Войти"]']  # кнопка "Войти" в форме регистрации
    ELEMENT_WITH_LOGIN_TEXT = (By.XPATH, "//*[text() = 'Вход']")  # элемент с текстом "Вход" на странице входа
    HISTORY_SHOP_BUTTON = (By.XPATH, "//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")  # кнопка "История заказов" в личном кабинете
    INFO_MESSAGE = (By.XPATH, "//p[contains(text(),'персональные данные')]")  # сообщение о том, что нужно заполнить персональные данные