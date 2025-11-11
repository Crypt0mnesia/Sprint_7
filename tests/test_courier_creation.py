import allure

@allure.epic("API Яндекс Самокат")
@allure.feature("Создание курьера")
class TestCourierCreation:


    @allure.story("Курьера можно создать")
    @allure.story("Запрос возвращает правильный код ответа")
    @allure.title("Успешное создание курьера - проверка кода 201")
    def test_create_courier_returns_correct_status_code(self, courier_api, courier_data):
        response = courier_api.create_courier(
            courier_data['login'],
            courier_data['password'],
            courier_data['firstName']
        )
        assert response.status_code == 201


    @allure.story("Курьера можно создать")
    @allure.story("Успешный запрос возвращает 'ok':true")
    @allure.title("Успешное создание курьера - проверка тела ответа")
    def test_create_courier_returns_correct_body(self, courier_api, courier_data):
        response = courier_api.create_courier(
            courier_data['login'],
            courier_data['password'],
            courier_data['firstName']
        )
        assert response.json() == {"ok": True}


    @allure.story("Нельзя создать двух одинаковых курьеров")
    @allure.title("Создание полного дубликата курьера")
    def test_create_duplicate_courier_fails(self, courier_api, registered_courier):
        login, password, first_name, courier_id = registered_courier
        response = courier_api.create_courier(login, password, first_name)
        assert response.status_code == 409


    @allure.story("Создание пользователя с существующим логином возвращает ошибку")
    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_with_existing_login_fails(self, courier_api, registered_courier):
        login, _, _, courier_id = registered_courier
        response = courier_api.create_courier(login, "different_password", "different_name")
        assert response.status_code == 409


    @allure.story("Чтобы создать курьера, нужно передать все обязательные поля")
    @allure.story("Если одного из полей нет, запрос возвращает ошибку")
    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login_fails(self, courier_api, courier_data):
        response = courier_api.create_courier("", courier_data['password'], courier_data['firstName'])
        assert response.status_code == 400


    @allure.story("Чтобы создать курьера, нужно передать все обязательные поля")
    @allure.story("Если одного из полей нет, запрос возвращает ошибку")
    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password_fails(self, courier_api, courier_data):
        response = courier_api.create_courier(courier_data['login'], "", courier_data['firstName'])
        assert response.status_code == 400
