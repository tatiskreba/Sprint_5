from locators import *
from selenium.webdriver.support import expected_conditions as EC
import conftest

class TestStellarBurgers:

    def test_button_bread(self, driver):
        conftest.wait_for_element_located(driver, time=10, locator=Locators.CONSTRUCTOR_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.SAUCES_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.BUN_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.BUN_BUTTON).click()
        assert 'tab_tab_type_current' in driver.find_element(*Locators.BUN_BUTTON).get_attribute('class')

    def test_button_sauces(self, driver):
        conftest.wait_for_element_located(driver, time=10, locator=Locators.CONSTRUCTOR_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        conftest.wait_for_element_located(driver, time=10, locator=Locators.SAUCES_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        assert 'tab_tab_type_current' in driver.find_element(*Locators.SAUCES_BUTTON).get_attribute('class')

    def test_button_filling(self, driver):
        conftest.wait_for_element_located(driver, time=10, locator=Locators.FILLING_BUTTON, condition=EC.presence_of_element_located)
        driver.find_element(*Locators.FILLING_BUTTON).click()
        assert 'tab_tab_type_current' in driver.find_element(*Locators.FILLING_BUTTON).get_attribute('class')
