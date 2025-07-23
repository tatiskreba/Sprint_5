from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from helper import *
from locators import Locators

class TestStellarBurgersRegistration:

    def test_success_registration(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ANY_FORMS))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.current_url == URL_MAIN_PAGE

    def test_failed_registration_with_short_password(self, driver):
        name, email, password = generate_registration_data_short_password()
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
        assert driver.find_element(*Locators.PASSWORD_ERROR).text == 'Некорректный пароль'