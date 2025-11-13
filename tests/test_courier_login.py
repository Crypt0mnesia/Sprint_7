import allure
from src.data import ExpectedResponses
from src.courier_api import CourierAPI
from src.data_generator import generate_courier_data


@allure.epic("API Яндекс Самокат")
@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.story("Курьер может авторизоваться")
    @allure.story("Успешный запрос возвращает id")
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, registered_courier):
        courier_api = CourierAPI()
        login, password, _, _ = registered_courier
        response = courier_api.login_courier(login, password)
        response_body = response.json()
        expected_status, _ = ExpectedResponses.SUCCESSFUL_LOGIN
        # Проверка для стори "Курьер может авторизоваться"
        with allure.step("Проверить что курьер может авторизоваться"):
            assert response.status_code == expected_status

        # Проверка для стори "Успешный запрос возвращает id"
        with allure.step("Проверить что запрос возвращает id"):
            assert "id" in response_body

    @allure.story("Для авторизации нужно передать все обязательные поля")
    @allure.story("Если какого-то поля нет, запрос возвращает ошибку")
    @allure.title("Логин без логина")
    def test_login_without_login_fails(self, registered_courier):
        courier_api = CourierAPI()
        _, password, _, _ = registered_courier
        response = courier_api.login_courier("", password)
        expected_status, expected_body = ExpectedResponses.MISSING_LOGIN_FIELD
        assert response.status_code == expected_status
        assert response.json() == expected_body

    @allure.story("Для авторизации нужно передать все обязательные поля")
    @allure.story("Если какого-то поля нет, запрос возвращает ошибку")
    @allure.title("Логин без пароля")
    def test_login_without_password_fails(self, registered_courier):
        courier_api = CourierAPI()
        login, _, _, _ = registered_courier
        response = courier_api.login_courier(login, "")
        expected_status, expected_body = ExpectedResponses.MISSING_LOGIN_FIELD
        assert response.status_code == expected_status
        assert response.json() == expected_body

    @allure.story("Система вернёт ошибку, если неправильно указать логин или пароль")
    @allure.title("Логин с неверным логином")
    def test_login_with_wrong_login_fails(self, registered_courier):
        courier_api = CourierAPI()
        login, password, _, _ = registered_courier
        response = courier_api.login_courier(login + "wrong", password)
        expected_status, expected_body = ExpectedResponses.ACCOUNT_NOT_FOUND
        assert response.status_code == expected_status
        assert response.json() == expected_body

    @allure.story("Система вернёт ошибку, если неправильно указать логин или пароль")
    @allure.title("Логин с неверным паролем")
    def test_login_with_wrong_password_fails(self, registered_courier):
        courier_api = CourierAPI()
        login, password, _, _ = registered_courier
        response = courier_api.login_courier(login, password + "wrong")
        expected_status, expected_body = ExpectedResponses.ACCOUNT_NOT_FOUND
        assert response.status_code == expected_status
        assert response.json() == expected_body

    @allure.story("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    @allure.title("Логин несуществующего курьера")
    def test_login_nonexistent_courier_fails(self):
        courier_api = CourierAPI()
        courier_data = generate_courier_data()
        response = courier_api.login_courier(courier_data['login'], courier_data['password'])
        expected_status, expected_body = ExpectedResponses.ACCOUNT_NOT_FOUND
        assert response.status_code == expected_status
        assert response.json() == expected_body




