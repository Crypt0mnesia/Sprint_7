import allure
from src.base_api import BaseAPI
from src.endpoints import ORDER_CREATE, ORDER_LIST

class OrderAPI(BaseAPI):
    @allure.step("Создать заказ")
    def create_order(self, order_data):
        return self.post(ORDER_CREATE, order_data)

    @allure.step("Получить список заказов")
    def get_orders_list(self):
        return self.get(ORDER_LIST)