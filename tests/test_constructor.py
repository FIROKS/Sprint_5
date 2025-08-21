from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
from data import Constants

class TestConstructor:
    def test_sauces_active_tab(self, driver):
        driver.find_element(*Locators.SAUCES_TAB).click()
        active_tab_text = WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB)).text

        assert Constants.SAUCES_TAB_TEXT in active_tab_text

    def test_buns_active_tab(self, driver):
        driver.find_element(*Locators.SAUCES_TAB).click()
        driver.find_element(*Locators.BUNS_TAB).click()
        active_tab_text = WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB)).text

        assert Constants.BUNS_TAB_TEXT in active_tab_text

    def test_fillings_active_tab(self, driver):
        driver.find_element(*Locators.FILLINGS_TAB).click()
        active_tab_text = WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB)).text

        assert Constants.FILLINGS_TAB_TEXT in active_tab_text