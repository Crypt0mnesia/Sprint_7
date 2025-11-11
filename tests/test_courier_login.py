import allure


@allure.epic("API Яндекс Самокат")
@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.story("Курьер может авторизоваться")
    @allure.story("Успешный запрос возвращает id")
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, registered_courier, courier_api):
        login, password, _, _ = registered_courier
        response = courier_api.login_courier(login, password)
        response_body = response.json()

        # Проверка для стори "Курьер может авторизоваться"
        with allure.step("Проверить что курьер может авторизоваться"):
            assert response.status_code == 200

        # Проверка для стори "Успешный запрос возвращает id"
        with allure.step("Проверить что запрос возвращает id"):
            assert "id" in response_body

    @allure.story("Для авторизации нужно передать все обязательные поля")
    @allure.story("Если какого-то поля нет, запрос возвращает ошибку")
    @allure.title("Логин без логина")
    def test_login_without_login_fails(self, registered_courier, courier_api):
        _, password, _, _ = registered_courier
        response = courier_api.login_courier("", password)
        assert response.status_code == 400
        assert response.json() == {
            "code":400,
            "message": "Недостаточно данных для входа"
        }

    @allure.story("Для авторизации нужно передать все обязательные поля")
    @allure.story("Если какого-то поля нет, запрос возвращает ошибку")
    @allure.title("Логин без пароля")
    def test_login_without_password_fails(self, registered_courier, courier_api):
        login, _, _, _ = registered_courier
        response = courier_api.login_courier(login, "")
        assert response.status_code == 400
        assert response.json() == {
            "code":400,
            "message": "Недостаточно данных для входа"
        }

    @allure.story("Система вернёт ошибку, если неправильно указать логин или пароль")
    @allure.title("Логин с неверным логином")
    def test_login_with_wrong_login_fails(self, registered_courier, courier_api):
        login, password, _, _ = registered_courier
        response = courier_api.login_courier(login + "wrong", password)
        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    @allure.story("Система вернёт ошибку, если неправильно указать логин или пароль")
    @allure.title("Логин с неверным паролем")
    def test_login_with_wrong_password_fails(self, registered_courier, courier_api):
        login, password, _, _ = registered_courier
        response = courier_api.login_courier(login, password + "wrong")
        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    @allure.story("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    @allure.title("Логин несуществующего курьера")
    def test_login_nonexistent_courier_fails(self, courier_api, courier_data):
        response = courier_api.login_courier(courier_data['login'], courier_data['password'])
        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена"
        }




