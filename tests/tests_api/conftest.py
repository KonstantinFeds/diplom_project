import os

import allure
import pytest
from dotenv import load_dotenv

import utils.file
from api.clients.user_api import UserApiMethods
from data.generators import generate_user_payload


@allure.title("api url")
@pytest.fixture()
def api_url():
    load_dotenv(dotenv_path=utils.file.abs_path_from_project(".env.config_project"))
    return os.getenv("API_URL")


@allure.title("request headers")
@pytest.fixture()
def headers():
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    return headers


@allure.title("Создание пользователя для тестов")
@pytest.fixture(scope="function")
def created_user(user_api_client):
    user_payload = generate_user_payload()

    create_user = user_api_client.post_create_user_request_body(user_payload)
    assert create_user.status_code == 200

    yield {
        "payload": user_payload,
        "username": user_payload["username"],
        "id": user_payload["id"],
        "password": user_payload["password"],
    }

    delete_user = user_api_client.delete_user(user_payload["username"])
    assert delete_user.status_code == 200


@allure.title("API клиент для пользователей")
@pytest.fixture()
def user_api_client(api_url, headers):
    return UserApiMethods(api_url, headers)
