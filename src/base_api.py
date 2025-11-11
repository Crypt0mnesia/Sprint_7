import json
import requests
import allure

from src.endpoints import BASE_URL


class BaseAPI:

    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {'Content-Type': 'application/json'}

    @allure.step("POST запрос к {endpoint}")
    def post(self, endpoint, payload):
        url = self.base_url + endpoint
        data = json.dumps(payload)
        return requests.post(url, data=data, headers=self.headers)

    @allure.step("GET запрос к {endpoint}")
    def get(self, endpoint, params=None):
        url = self.base_url + endpoint
        return requests.get(url, params=params, headers=self.headers)

    @allure.step("DELETE запрос к {endpoint}")
    def delete(self, endpoint):
        url = self.base_url + endpoint
        return requests.delete(url, headers=self.headers)