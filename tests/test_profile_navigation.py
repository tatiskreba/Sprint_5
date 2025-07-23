from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from data import Credentials
from locators import Locators

class TestStellarBurgersProfileNavigation:

    def test_transit_to_personal_account_authorized(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        assert driver.current_url == URL_PROFILE

    def test_transit_to_personal_account_no_authorized(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_BUTTON))
        assert driver.current_url == URL_LOGIN