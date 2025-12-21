import pytest
from faker import Faker
from tests.api.data.generators import payload_generate_user

fake = Faker()

@pytest.fixture()
def api_url():
    return 'https://petstore.swagger.io'

@pytest.fixture()
def headers():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    return headers

@pytest.fixture(scope="session")
def user_payload():
    return payload_generate_user()


@pytest.fixture()
def common_username(user_payload):
    return user_payload['username']

@pytest.fixture()
def common_password(user_payload):
    return user_payload['password']

@pytest.fixture()
def common_id(user_payload):
    return user_payload['id']

