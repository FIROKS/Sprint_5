import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials, Constants
from locators import Locators
from endpoints import Endpoints
from helper import get_endpoint

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(get_endpoint(Endpoints.MAIN_PAGE))
    yield driver

    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(get_endpoint(Endpoints.LOGIN_PAGE))
    WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.EMAIL))
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.EXISTING_EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.CORRECT_PASSWORD)
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()

    return driver
