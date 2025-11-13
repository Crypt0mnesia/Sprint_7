import pytest
import allure
from src.courier_api import CourierAPI
from src.data_generator import generate_courier_data


@pytest.fixture
def created_courier_response():
    courier_api = CourierAPI()
    courier_data = generate_courier_data()

    response = courier_api.create_courier(
        courier_data['login'],
        courier_data['password'],
        courier_data['firstName']
    )

    login_response = courier_api.login_courier(
        courier_data['login'],
        courier_data['password']
    )
    courier_id = login_response.json().get('id')

    yield response

    courier_api.delete_courier(courier_id)


@pytest.fixture
def registered_courier():
    courier_api = CourierAPI()
    courier_data = generate_courier_data()
    with allure.step("Создать курьера"):
        courier_api.create_courier(
            courier_data['login'],
            courier_data['password'],
            courier_data['firstName']
        )

    with allure.step("Получить ID курьера"):
        login_response = courier_api.login_courier(
            courier_data['login'],
            courier_data['password']
        )
        courier_id = login_response.json().get('id')

    yield courier_data['login'], courier_data['password'], courier_data['firstName'], courier_id

    with allure.step("Удалить курьера"):
        courier_api.delete_courier(courier_id)
