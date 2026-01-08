import allure
from api.json_schemas.assertions import UserAssertions
from api.json_schemas.validators import SchemaValidator


@allure.epic("авторизация")
@allure.title("успешная авторизация пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_login_user_success(user_payload, user_api, headers):

    user_api.post_create_user_request_body(user_payload)

    username = user_payload["username"]
    password = user_payload["password"]

    response_get = user_api.get_user_login(username, password)
    assert response_get.status_code == 200
    SchemaValidator.validate_schema(response_get.json(), "responses/get_login_response.json")
    UserAssertions.assert_get_user_login_response_body(response_get.json())

    user_api.delete_user(username)
