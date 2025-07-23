from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from data import Credentials
from locators import Locators

class TestStellarBurgersLoginLogoutForm:

    def test_login_sign_in_button_show_login_page(self, driver):
        driver.find_element(*Locators.AUTH).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)
        assert driver.current_url == URL_MAIN_PAGE and order_button.text == 'Оформить заказ'

    def test_login_personal_account_button_show_login_page(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.current_url == URL_MAIN_PAGE

    def test_login_registration_form_sign_in_button(self, driver):
        driver.get(URL_REGISTER)
        driver.find_element(*Locators.FORM_LOGIN_TEXT).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD.send_keys(Credentials.PASSWORD))
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.current_url == URL_MAIN_PAGE

    def test_login_forgot_password_form_sign_in_button(self, driver):
        driver.get(URL_FORGOT_PASSWORD)
        driver.find_element(*Locators.LOGIN_TEXT_WITH_HREF).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.current_url == URL_MAIN_PAGE