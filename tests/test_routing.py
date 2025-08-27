from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from endpoints import Endpoints
from locators import Locators
from data import Constants
from helper import get_endpoint

class TestRouting:
    def test_go_to_profile(self, login):
        driver = login
        driver.find_element(*Locators.PROFILE_LINK).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert driver.current_url == get_endpoint(Endpoints.PROFILE_PAGE)

    def test_go_to_constructor(self, login):
        driver = login
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_LINK))
        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()
        assert driver.current_url == get_endpoint(Endpoints.MAIN_PAGE)
