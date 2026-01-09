import allure
import requests

from utils.logger import response_logging, response_attaching


class UserApiMethods:

    def __init__(self, api_url: str, headers: dict):
        self.api_url = api_url
        self.headers = headers

    @allure.step("создание пользователя")
    def post_create_user_request_body(self, user_payload):
        response = requests.request(
            method="POST",
            url=f"{self.api_url}/v2/user/",
            headers=self.headers,
            json=user_payload,
            timeout=10,
        )

        response_logging(response)
        response_attaching(response)

        return response

    @allure.step("получение пользователя по username")
    def get_user_by_username(self, username: str):
        response = requests.request(
            method="GET",
            url=f"{self.api_url}/v2/user/{username}",
            headers=self.headers,
            timeout=10,
        )

        response_logging(response)
        response_attaching(response)

        return response

    @allure.step("обновление данных пользователя")
    def put_update_user_request_body(self, username: str, user_payload: dict):
        response = requests.request(
            method="PUT",
            url=f"{self.api_url}/v2/user/{username}",
            headers=self.headers,
            json=user_payload,
            timeout=10,
        )

        response_logging(response)
        response_attaching(response)

        return response

    @allure.step("логин пользователя")
    def get_user_login(self, username: str, password: str):
        response = requests.request(
            method="GET",
            url=f"{self.api_url}/v2/user/login",
            headers=self.headers,
            params={"username": username, "password": password},
            timeout=10,
        )
        response_logging(response)
        response_attaching(response)

        return response

    @allure.step("разлогин пользователя")
    def get_user_logout(self):
        response = requests.request(
            method="GET",
            url=f"{self.api_url}/v2/user/logout",
            headers=self.headers,
            timeout=10,
        )
        response_logging(response)
        response_attaching(response)

        return response

    @allure.step("удаление пользователя")
    def delete_user(self, username: str):
        response = requests.request(
            method="DELETE",
            url=f"{self.api_url}/v2/user/{username}",
            headers=self.headers,
            timeout=10,
        )

        response_logging(response)
        response_attaching(response)

        return response
