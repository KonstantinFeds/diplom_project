import allure
from data.json_schemas.validators import SchemaValidator


@allure.epic("удаление пользователя")
@allure.title("успешное удаление пользователя")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_user_success(user_api, headers, user_payload):

    user_api.post_create_user_request_body(user_payload)

    username = user_payload["username"]

    delete_response = user_api.delete_user(username)
    assert delete_response.status_code == 200

    SchemaValidator.validate_schema(delete_response.json(), "delete_user_response.json")

    response_body = delete_response.json()
    assert response_body["code"] == 200
    assert response_body["type"] == "unknown"
    assert response_body["message"] == username

    get_response = user_api.get_user_by_username(username)
    assert get_response.status_code == 404
