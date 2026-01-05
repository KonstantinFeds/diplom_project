import allure
from data.json_schemas.assertions import UserAssertions
from data.json_schemas.validators import SchemaValidator


@allure.epic("получение пользователя")
@allure.title("успешное получение пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user_by_user_name_success(user_api, headers, user_payload):

    user_api.post_create_user_request_body(user_payload)

    username = user_payload["username"]

    get_response = user_api.get_user_by_username(username)

    assert get_response.status_code == 200
    SchemaValidator.validate_schema(get_response.json(),'get_user_response.json')
    UserAssertions.assert_get_user_response_body(get_response.json(),user_payload)

    user_api.delete_user(username)
