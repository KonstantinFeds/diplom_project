import allure
import pytest
import config
from pages.api.user_api import UserApiMethods
from data.generators import payload_generate_user, generate_password




@pytest.fixture(scope="session", autouse=True)
def clean_allure_results():
    config.clear_allure_results()


@allure.title("api url")
@pytest.fixture()
def api_url():
    return "https://petstore.swagger.io"


@allure.title("request headers")
@pytest.fixture()
def headers():
    headers = {"accept": "application/json", "Content-Type": "application/json"}

    return headers


@allure.title("генерация payload")
@pytest.fixture(scope="function")
def user_payload():
    return payload_generate_user()

@allure.title("API клиент для пользователей")
@pytest.fixture()
def user_api(api_url, headers):
    return UserApiMethods(api_url, headers)


