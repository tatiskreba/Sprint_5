from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from data import Credentials
from locators import Locators

class TestStellarBurgersLogout:

    def test_click_logout_button_in_lk_open_login_form(self, driver):
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ANY_FORMS))
        assert driver.current_url == URL_LOGIN