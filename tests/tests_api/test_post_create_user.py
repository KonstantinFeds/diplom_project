import allure
from pages.api.user_api import UserApiMethods
from data.json_schemas.validators import SchemaValidator


@allure.epic("создание пользователя")
@allure.title("успешное создание пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_create_user_success(user_api, headers, user_payload):


    SchemaValidator.validate_schema(data_to_validate=user_payload,
        schema_filename="post_create_user_payload.json"
    )

    create_response = user_api.post_create_user_request_body(user_payload)
    assert create_response.status_code == 200

    SchemaValidator.validate_schema(create_response.json(),'post_create_user_response.json')


    response_body = create_response.json()
    expected_message = str(user_payload["id"])
    assert response_body["code"] == 200
    assert response_body["type"] == "unknown"
    assert response_body["message"] == expected_message

    username = user_payload["username"]

    user_api.delete_user(username)
