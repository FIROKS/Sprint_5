from selenium.webdriver.common.by import By

class Locators:
    # Поле email
    EMAIL = (By.XPATH, '//div[contains(@class, "input")]/label[text()="Email"]/following-sibling::input')
    # Поле пароль
    PASSWORD = [By.XPATH, '//div[contains(@class, "input")]/input[@type="password"]']
    # Контейнер поля ввода пароля
    PASSWORD_CONTAINER = [By.XPATH, '//div[contains(@class, "input")]/input[@type="password"]/parent::*']
    # Сообщение о неправильном пароле
    WRONG_PASSWORD_MESSAGE = [By.XPATH, '//div[contains(@class, "input")]/input[@type="password"]/following::p[1]']
    # Поле Имя
    NAME = [By.XPATH, '//div[contains(@class, "input")]/label[text()="Имя"]/following-sibling::input']
    

    # Ссылка "Личный Кабинет" на главной странице
    PROFILE_LINK = [By.XPATH, '//a[@href="/account"]']
    # Ссылка 'Зарегистрироваться' на странице входа
    REGISTRATION_LINK = [By.LINK_TEXT, 'Зарегистрироваться']
    # Кнопка "Войти в аккаунт" на главной странице
    SIGN_IN_ACCOUNT_BUTTON = [By.XPATH, '//button[text()="Войти в аккаунт"]']
    # Кнопка "Войти" на странице входа 
    SIGN_IN_BUTTON = [By.XPATH, '//form[starts-with(@class, "Auth")]/button[text()="Войти"]']
    # Кнопка "Зарегистрироваться" на странице регистрации 
    SIGN_UP_BUTTON = [By.XPATH, '//form[starts-with(@class, "Auth")]/button[text()="Зарегистрироваться"]']
    # Кнопка "Выход" на странице профиля
    SIGN_OUT_BUTTON = [By.XPATH, '//ul[contains(@class, "Account_list")]/li/button[text()="Выход"]']
    # Кнопка "Профиль" в личном кабинете
    PROFILE_BUTTON = (By.XPATH, '//a[@href="/account/profile"]')
    # Кнопка "Войти" на странице восстановления пароля 
    RECALL_PASSWORD_SIGN_IN_BUTTON = [By.XPATH, '//p[text()="Вспомнили пароль?"]/a']
    # Кнопка "Войти" на странице регистрации
    REGISTRATION_SIGN_IN_BUTTON = [By.XPATH, '//p[text()="Уже зарегистрированы?"]/a']
    # Ссылка на страницу конструктора
    CONSTRUCTOR_LINK = [By.XPATH, '//a[contains(@class, "AppHeader_header__link")]']
    # Кнопка "Булки" на странице конструктора
    BUNS_TAB = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]//span[text()="Булки"]')
    # Кнопка "Соусы" на странице конструктора
    SAUCES_TAB = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]//span[text()="Соусы"]')
    # Кнопка "Начинки" на странице конструктора
    FILLINGS_TAB = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]//span[text()="Начинки"]')
    # Активная вкладка в конструкторе
    ACTIVE_TAB = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]//div[contains(@class, "tab_tab_type_current")]')
