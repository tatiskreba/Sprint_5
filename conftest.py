import pytest
from selenium import webdriver
from urls import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL_MAIN_PAGE)
    yield driver
    driver.quit()

