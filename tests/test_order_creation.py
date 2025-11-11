import pytest
import allure
from src.data_generator import generate_order_data


@allure.epic("API Яндекс Самокат")
@allure.feature("Создание заказа")
class TestOrderCreation:

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"]
    ])
    @allure.story("Можно указать один из цветов — BLACK или GREY")
    @allure.title("Создание заказа с одним цветом: {color}")
    def test_create_order_with_single_color(self, order_api, color):
        order_data = generate_order_data(color=color)
        response = order_api.create_order(order_data)
        assert response.status_code == 201

    @allure.story("Можно указать оба цвета")
    @allure.title("Создание заказа с обоими цветами")
    def test_create_order_with_both_colors(self, order_api):
        order_data = generate_order_data(color=["BLACK", "GREY"])
        response = order_api.create_order(order_data)
        assert response.status_code == 201

    @allure.story("Можно совсем не указывать цвет")
    @allure.title("Создание заказа без цвета")
    def test_create_order_without_color(self, order_api):
        order_data = generate_order_data(color=None)
        response = order_api.create_order(order_data)
        assert response.status_code == 201

    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.story("Тело ответа содержит track")
    @allure.title("Проверка наличия track для цвета: {color}")
    def test_create_order_returns_track(self, order_api, color):
        order_data = generate_order_data(color=color if color else None)
        response = order_api.create_order(order_data)
        response_body = response.json()
        assert "track" in response_body


