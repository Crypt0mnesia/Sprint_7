import allure
from src.base_api import BaseAPI
from src.endpoints import COURIER_LOGIN, COURIER_CREATE, COURIER_DELETE


class CourierAPI(BaseAPI):
    @allure.step("Создать курьера")
    def create_courier(self, login, password, first_name):
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        return self.post(COURIER_CREATE, payload)

    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        payload = {
            'login': login,
            'password': password
        }
        return self.post(COURIER_LOGIN, payload)

    @allure.step("Удалить курьера с ID {courier_id}")
    def delete_courier(self, courier_id):
        return self.delete(COURIER_DELETE+str(courier_id))