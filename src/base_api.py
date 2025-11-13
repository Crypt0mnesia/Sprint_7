import json
import requests
import allure

class BaseAPI:

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    @allure.step("POST запрос к {endpoint}")
    def post(self, endpoint, payload):
        data = json.dumps(payload)
        return requests.post(endpoint, data=data, headers=self.headers)

    @allure.step("GET запрос к {endpoint}")
    def get(self, endpoint, params=None):
        return requests.get(endpoint, params=params, headers=self.headers)

    @allure.step("DELETE запрос к {endpoint}")
    def delete(self, endpoint):
        return requests.delete(endpoint, headers=self.headers)