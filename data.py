from helper import generate_email

class Credentials:
    NAME = 'Maxim'
    EXISTING_EMAIL ='Maxim_Ap_26_123@yandex.ru'
    GENERATED_EMAIL= generate_email()
    CORRECT_PASSWORD ='1a2b3c'
    WRONG_LENGTH_PASSWORD = 'A'

class Constants:
    TIMEOUT = 10
    WRONG_PASSWORD_MESSAGE_TEXT = 'Некорректный пароль'
    WRONG_INPUT_CLASS = 'input_status_error'
    BUNS_TAB_TEXT = 'Булки'
    SAUCES_TAB_TEXT = 'Соусы'
    FILLINGS_TAB_TEXT = 'Начинки'