from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from data import Credentials
from locators import Locators

class TestStellarBurgersConstructorNavigation:

    def test_click_constructor_button_show_constructor_form(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_CONT))
        assert driver.current_url == URL_MAIN_PAGE

    def test_transit_from_personal_account_to_stellar_logo(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.current_url == URL_MAIN_PAGE