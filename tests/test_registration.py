import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import Urls
from data import ValidData
import conftest

class TestStellarBurgersRegistration:

    def test_successful_registration(self, driver): # успешная регистрация
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.NAME_FIELD).send_keys(ValidData.USER_NAME)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(ValidData.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(ValidData.PASSWORD)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.ELEMENT_WITH_LOGIN_TEXT, condition=EC.presence_of_element_located)
        login_button = driver.find_element(*Locators.ELEMENT_WITH_LOGIN_TEXT)
        assert driver.current_url == Urls.URL_LOGIN and login_button.text == 'Вход'

    def test_registration_empty_name(self, driver):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('test1@ya.ru')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('124567')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.REGISTER_BUTTON, condition=EC.presence_of_element_located)
        errors_messages = driver.find_elements(*Locators.ERROR_MESSAGE)
        assert driver.current_url == Urls.URL_REGISTER and len(errors_messages) == 0

    def test_registration_empty_email(self, driver):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('test1@ya.ru')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('124567')
        register_button = driver.find_element(*Locators.REGISTER_BUTTON)
        register_button.click()
        assert driver.current_url == Urls.URL_REGISTER
        errors_messages = driver.find_elements(*Locators.ERROR_MESSAGE)
        assert len(errors_messages) == 0

    @pytest.mark.parametrize('email_list', [
        'missingatsign.com',
        'missingdomain@',
        '@missinguser.com',
        'user@.invalid',
        'user@domain,com',
        'user@domain@domain.com',
        'user@.com'
    ])

    def test_registration_invalid_email(self, driver, email_list):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.NAME_FIELD).send_keys('Скребцова Татьяна')
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email_list)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.ERROR_MESSAGE_TWO, condition=EC.presence_of_element_located)
        error_message = driver.find_element(*Locators.ERROR_MESSAGE_TWO)
        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password_list', [
        '1',
        '12345'
    ])

    def test_registration_short_password(self, driver, password_list):
        driver.get(Urls.URL_REGISTER)
        driver.find_element(*Locators.NAME_FIELD).send_keys('Скребцова Тати')
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('test1@ya.ru')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password_list)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.ERROR_MESSAGE, condition=EC.presence_of_element_located)
        error_message = driver.find_element(*Locators.ERROR_MESSAGE)
        assert error_message.text == 'Некорректный пароль'