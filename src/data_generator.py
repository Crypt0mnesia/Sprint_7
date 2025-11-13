import requests
import random
import string
from src.endpoints import COURIER_CREATE


def _generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier_and_return_login_password():
    login_pass = []
    login = _generate_random_string(10)
    password = _generate_random_string(10)
    first_name = _generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(COURIER_CREATE, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

def generate_courier_data():
    return {
        'login': _generate_random_string(10),
        'password': _generate_random_string(10),
        'firstName': _generate_random_string(10)
    }

def generate_order_data(color=None):

    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Тверская, д. 15",
        "metroStation": "Тверская",
        "phone": "+79001234567",
        "rentTime": 3,
        "deliveryDate": "2025-11-10",
        "comment": "Позвонить перед доставкой"
    }

    if color is not None:
        order_data["color"] = color

    return order_data

