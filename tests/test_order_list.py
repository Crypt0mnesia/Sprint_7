import allure


@allure.epic("API Яндекс Самокат")
@allure.feature("Список заказов")
class TestOrderList:

    @allure.story("В тело ответа возвращается список заказов")
    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_orders(self, order_api):
        response = order_api.get_orders_list()
        response_body = response.json()
        assert isinstance(response_body["orders"], list)
