from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Constants
from locators import Locators
from endpoints import Endpoints
from helper import get_endpoint

class TestSignout:
    def test_sign_out(self, login):
        driver = login
        driver.find_element(*Locators.PROFILE_LINK).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.SIGN_OUT_BUTTON))
        # Выходим из аккаунта
        driver.find_element(*Locators.SIGN_OUT_BUTTON).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        # Кликаем на кнопку "Личный кабинет"
        driver.find_element(*Locators.PROFILE_LINK).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.SIGN_IN_BUTTON))
        assert driver.current_url == get_endpoint(Endpoints.LOGIN_PAGE)
