from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import Urls
from data import Credentials
import conftest

class TestStellarBurgersLoginLogoutForm:

    def test_login_correct_email_and_password_show_main_page(self, login, driver):
        driver = login
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url.startswith(Urls.URL_MAIN_PAGE) and order_button.text == 'Оформить заказ'

    def test_login_sign_in_button_show_login_page(self, driver):
        driver.find_element(*Locators.AUTH).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.LOGIN_BUTTON_ANY_FORMS, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.ORDER_BUTTON,condition=EC.presence_of_element_located)
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url.startswith(Urls.URL_MAIN_PAGE) and order_button.text == 'Оформить заказ'

    def test_login_personal_account_button_show_login_page(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.LOGIN_BUTTON_ANY_FORMS, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.ORDER_BUTTON, condition=EC.presence_of_element_located)
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url.startswith(Urls.URL_MAIN_PAGE) and order_button.text == 'Оформить заказ'

    def test_login_registration_form_sign_in_button(self, driver):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.LOGIN_TEXT_WITH_HREF).click()
        conftest.wait_for_element_located(driver, time=15, locator=Locators.LOGIN_BUTTON_ANY_FORMS, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        conftest.wait_for_element_located(driver, time=20, locator=Locators.ORDER_BUTTON, condition=EC.presence_of_element_located)
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url.startswith(Urls.URL_MAIN_PAGE) and order_button.text == 'Оформить заказ'

    def test_login_forgot_password_form_sign_in_button(self, driver):
        driver.get(Urls.URL_FORGOT_PASSWORD)
        driver.find_element(*Locators.LOGIN_TEXT_WITH_HREF).click()
        conftest.wait_for_element_located(driver, time=20, locator=Locators.LOGIN_BUTTON_ANY_FORMS, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        conftest.wait_for_element_located(driver, time=20, locator=Locators.ORDER_BUTTON, condition=EC.presence_of_element_located)
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url.startswith(Urls.URL_MAIN_PAGE) and order_button.text == 'Оформить заказ'