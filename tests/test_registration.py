from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from endpoints import Endpoints
from data import Credentials, Constants
from locators import Locators
from helper import get_endpoint

class TestRegistration:
    def test_success_registration(self, driver):
        driver.get(get_endpoint(Endpoints.REGISTATION_PAGE))
        # Вводим корректные данные и кликаем на кнопку "Зарегистрироваться"
        driver.find_element(*Locators.NAME).send_keys(Credentials.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.GENERATED_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.CORRECT_PASSWORD)
        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
        # Очищаем поля ввода, заполняем данными и кликаем на кнопку "Войти"
        driver.get(get_endpoint(Endpoints.LOGIN_PAGE))
        email_input = driver.find_element(*Locators.EMAIL)
        password_input = driver.find_element(*Locators.PASSWORD)

        email_input.clear()
        email_input.send_keys(Credentials.GENERATED_EMAIL)
        password_input.clear()
        password_input.send_keys(Credentials.CORRECT_PASSWORD)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        # Переходим на страницу профиля
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.PROFILE_LINK).click()
        profile_button = WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.PROFILE_BUTTON)).text

        assert profile_button == 'Профиль'

    def test_show_wrong_password_message(self, driver):
        driver.get(get_endpoint(Endpoints.REGISTATION_PAGE))
        driver.find_element(*Locators.NAME).send_keys(Credentials.NAME)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.WRONG_LENGTH_PASSWORD)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.EXISTING_EMAIL)

        error_class = driver.find_element(*Locators.PASSWORD_CONTAINER).get_attribute('class')
        error_message = driver.find_element(*Locators.WRONG_PASSWORD_MESSAGE).text
        WebDriverWait(driver, Constants.TIMEOUT).until(EC.visibility_of_element_located(Locators.WRONG_PASSWORD_MESSAGE))

        assert Constants.WRONG_INPUT_CLASS in error_class
        assert error_message == Constants.WRONG_PASSWORD_MESSAGE_TEXT