import random
from endpoints import Endpoints

def generate_email():
    return f'Maxim_Ap_26_{random.randint(0, 999)}@yandex.ru'

def get_endpoint(endpoint):
    if endpoint == Endpoints.MAIN_PAGE:
        return Endpoints.MAIN_PAGE
    else:
        return Endpoints.MAIN_PAGE + endpoint
