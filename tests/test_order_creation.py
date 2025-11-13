import pytest
import allure
from src.order_api import OrderAPI
from src.data_generator import generate_order_data
from src.data import ExpectedResponses

@allure.epic("API Яндекс Самокат")
@allure.feature("Создание заказа")
class TestOrderCreation:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.story("Можно указать один из цветов — BLACK или GREY, оба цвета или не указывать цвет")
    @allure.title("Создание заказа с разными вариантами цветов: {color}")
    def test_create_order_with_different_colors(self, color):
        """Проверяем возможность создания заказа с разными вариантами цветов"""
        order_api = OrderAPI()
        with allure.step("Подготовить данные заказа"):
            order_data = generate_order_data(color=color if color else None)

        with allure.step("Создать заказ"):
            response = order_api.create_order(order_data)
            response_body = response.json()

        expected_status, _ = ExpectedResponses.SUCCESSFUL_ORDER_CREATION

        with allure.step("Проверить код ответа 201"):
            assert response.status_code == expected_status

        with allure.step("Проверить наличие track в теле ответа"):
            assert "track" in response_body

        with allure.step("Проверить что track является числом"):
            assert isinstance(response_body["track"], int)

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.story("Тело ответа содержит track")
    @allure.title("Проверка наличия track в ответе для заказа с цветом: {color}")
    def test_create_order_returns_track(self, color):
        """Проверяем что тело ответа содержит track для всех вариантов заказов"""

        order_api = OrderAPI()

        with allure.step("Подготовить данные заказа"):
            order_data = generate_order_data(color=color if color else None)

        with allure.step("Создать заказ"):
            response = order_api.create_order(order_data)
            response_body = response.json()

        expected_status, _ = ExpectedResponses.SUCCESSFUL_ORDER_CREATION

        with allure.step("Проверить код ответа 201"):
            assert response.status_code == expected_status

        with allure.step("Проверить наличие track в теле ответа"):
            assert "track" in response_body

        with allure.step("Проверить что track является числом"):
            assert isinstance(response_body["track"], int)



