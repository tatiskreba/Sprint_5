from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import Urls
import conftest

class TestStellarBurgersLogout:

    def test_click_logout_button_in_lk_open_login_form(self, driver, login):
        driver = login
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.INFO_MESSAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        conftest.wait_for_element_located(driver, time=8, locator=Locators.LOGIN_TEXT, condition=EC.presence_of_element_located)
        login_button = driver.find_element(*Locators.ELEMENT_WITH_LOGIN_TEXT)
        assert driver.current_url == Urls.URL_LOGIN and login_button.text == 'Вход'