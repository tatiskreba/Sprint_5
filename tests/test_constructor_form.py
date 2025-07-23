from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from urls import URL_MAIN_PAGE

class TestBurgerConstructor:

    def test_button_sauces(self, driver):
        driver.get(URL_MAIN_PAGE)
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        active_tab = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.ACTIV_TAB))
        assert active_tab.text == 'Соусы'

    def test_button_filling(self, driver):
        driver.get(URL_MAIN_PAGE)
        driver.find_element(*Locators.FILLING_BUTTON).click()
        active_tab = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.ACTIV_TAB))
        assert active_tab.text == 'Начинки'

    def test_button_buns(self, driver):
        driver.find_element(*Locators.FILLING_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.SAUCES))
        driver.find_element(*Locators.BUN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUN))
        activ_tab = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACTIV_TAB))
        assert activ_tab.text == 'Булки'

