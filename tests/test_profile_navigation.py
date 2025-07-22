from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import Urls
import conftest

class TestStellarBurgersProfileNavigation:

    def test_click_profile_button_open_profile_form(self, driver, login):
        driver = login
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.INFO_MESSAGE, condition=EC.presence_of_element_located)
        profile = driver.find_element(*Locators.HISTORY_SHOP_BUTTON)
        assert Urls.URL_PROFILE == driver.current_url and profile.text == 'История заказов'