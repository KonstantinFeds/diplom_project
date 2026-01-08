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


@allure.title("генерация payload")
@pytest.fixture(scope="function")
def user_payload():
    return generate_user_payload()


@allure.title("API клиент для пользователей")
@pytest.fixture()
def user_api(api_url, headers):
    return UserApiMethods(api_url, headers)
