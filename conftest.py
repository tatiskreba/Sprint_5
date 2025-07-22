import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from locators import *
from urls import Urls
from data import Credentials

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1280,800")
    driver = webdriver.Chrome(options=options)
    driver.get(Urls.URL_MAIN_PAGE)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(Urls.URL_LOGIN)
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Credentials.LOGIN)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Credentials.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON_ANY_FORMS).click()
    wait_for_element_located(driver, time=10, locator=Locators.ORDER_BUTTON, condition=EC.presence_of_element_located)
    return driver

def wait_for_element_located(driver, locator, time, condition):
    return WebDriverWait(driver, time).until(condition(locator))