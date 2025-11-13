import allure
from src.order_api import OrderAPI
from src.data import ExpectedResponses

@allure.epic("API Яндекс Самокат")
@allure.feature("Список заказов")
class TestOrderList:

    @allure.story("В тело ответа возвращается список заказов")
    @allure.title("Получение списка заказов - проверка кода ответа и наличия списка заказов")
    def test_get_orders_list_returns_orders(self):

        order_api = OrderAPI()

        with allure.step("Получить список заказов"):
            response = order_api.get_orders_list()
            response_body = response.json()

        expected_status, _ = ExpectedResponses.SUCCESSFUL_ORDER_LIST

        with allure.step("Проверить код ответа 200"):
            assert response.status_code == expected_status

        with allure.step("Проверить что в ответе есть список заказов"):
            assert "orders" in response_body
            assert isinstance(response_body["orders"], list)
