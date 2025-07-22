from selenium.webdriver.support import expected_conditions as EC
from locators import *
import conftest

class TestStellarBurgersConstructorNavigation:

    def test_click_constructor_button_show_constructor_form(self, driver, login):
        driver = login
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.INFO_MESSAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(self, driver, login):
        driver = login
        driver.find_element(*Locators.PROFILE_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.INFO_MESSAGE, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.LOGO).click()
        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'