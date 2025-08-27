from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from endpoints import Endpoints
from locators import Locators
from data import Constants, Credentials
from helper import get_endpoint

class TestSignin:
    def test_sign_in_by_using_sign_in_account_button(self, driver):
        driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.EMAIL))

        # Входим в аккаунт
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.CORRECT_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        # Переходим на страницу профиля
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.PROFILE_LINK).click()

        assert WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))


    def test_sign_in_by_using_profile_link(self, driver):
        driver.find_element(*Locators.PROFILE_LINK).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.EMAIL))

        # Входим в аккаунт
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.CORRECT_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        # Переходим на страницу профиля
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.PROFILE_LINK).click()
        
        assert WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))


    def test_sign_in_by_using_sign_up_button(self, driver):
        # Переходим на страницу регистрации и кликаем кнопку "Войти"
        driver.get(get_endpoint(Endpoints.REGISTATION_PAGE))

        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.REGISTRATION_SIGN_IN_BUTTON))
        driver.find_element(*Locators.REGISTRATION_SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.EMAIL))

        # Входим в аккаунт
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.CORRECT_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        # Переходим на страницу профиля
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.PROFILE_LINK).click()
        
        assert WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))

    def test_sign_in_by_using_recall_password_sign_in_button(self, driver):
        # Переходим на страницу восстановления пароля и кликаем кнопку "Войти"
        driver.get(get_endpoint(Endpoints.RECOVER_PASSWORD_PAGE))

        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.RECALL_PASSWORD_SIGN_IN_BUTTON))
        driver.find_element(*Locators.RECALL_PASSWORD_SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.EMAIL))

        # Входим в аккаунт
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EXISTING_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.CORRECT_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        # Переходим на страницу профиля
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.PROFILE_LINK).click()
        
        assert WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON))