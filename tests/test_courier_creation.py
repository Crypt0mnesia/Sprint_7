import allure
from src.courier_api import CourierAPI
from src.data_generator import generate_courier_data
from src.data import ExpectedResponses


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание курьера")
class TestCourierCreation:

    @allure.story("Курьера можно создать")
    @allure.story("Запрос возвращает правильный код ответа")
    @allure.story("Успешный запрос возвращает 'ok':true")
    @allure.title("Успешное создание курьера - проверка кода и тела ответа")
    def test_create_courier_returns_correct_body(self, created_courier_response):
        courier_api = CourierAPI()
        courier_data = generate_courier_data()
        with allure.step("Создать курьера"):
            response = courier_api.create_courier(
                courier_data['login'],
                courier_data['password'],
                courier_data['firstName']
            )
        expected_status, expected_body = ExpectedResponses.SUCCESSFUL_CREATION

        with allure.step("Проверить код ответа 201"):
            assert response.status_code == expected_status
        with allure.step("Проверить тело ответа"):
            assert response.json() == expected_body

    @allure.story("Нельзя создать двух одинаковых курьеров")
    @allure.title("Создание полного дубликата курьера")
    def test_create_duplicate_courier_fails(self, registered_courier):
        courier_api = CourierAPI()
        login, password, first_name, courier_id = registered_courier
        response = courier_api.create_courier(login, password, first_name)
        expected_status, expected_body = ExpectedResponses.DUPLICATE_COURIER
        assert response.status_code == expected_status
        assert response.json() == expected_body

    @allure.story("Создание пользователя с существующим логином возвращает ошибку")
    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_with_existing_login_fails(self, registered_courier):
        courier_api = CourierAPI()
        login, _, _, courier_id = registered_courier
        response = courier_api.create_courier(login, "different_password", "different_name")
        expected_status, expected_body = ExpectedResponses.DUPLICATE_COURIER
        assert response.status_code == expected_status
        assert response.json() == expected_body

    @allure.story("Чтобы создать курьера, нужно передать все обязательные поля")
    @allure.story("Если одного из полей нет, запрос возвращает ошибку")
    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login_fails(self):
        courier_api = CourierAPI()
        courier_data = generate_courier_data()
        response = courier_api.create_courier("", courier_data['password'], courier_data['firstName'])
        expected_status, expected_body = ExpectedResponses.MISSING_REQUIRED_FIELD
        assert response.status_code == expected_status
        assert response.json() == expected_body

    @allure.story("Чтобы создать курьера, нужно передать все обязательные поля")
    @allure.story("Если одного из полей нет, запрос возвращает ошибку")
    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password_fails(self):
        courier_api = CourierAPI()
        courier_data = generate_courier_data()
        response = courier_api.create_courier(courier_data['login'], "", courier_data['firstName'])
        expected_status, expected_body = ExpectedResponses.MISSING_REQUIRED_FIELD
        assert response.status_code == expected_status
        assert response.json() == expected_body