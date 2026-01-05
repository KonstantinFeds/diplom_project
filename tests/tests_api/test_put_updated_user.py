import allure
from data.json_schemas.assertions import UserAssertions
from data.json_schemas.validators import SchemaValidator
from data.generators import generate_update_payload


@allure.epic("обновление пользователя")
@allure.title("успешное обновление пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_put_update_user_success(user_api, headers, user_payload):

    user_api.post_create_user_request_body(user_payload)

    old_username = user_payload["username"]

    update_payload = generate_update_payload(user_payload)

    SchemaValidator.validate_schema(
        data_to_validate=update_payload, schema_filename="put_user_payload.json"
    )

    response_put = user_api.put_update_user_request_body(old_username, update_payload)

    assert response_put.status_code == 200

    SchemaValidator.validate_schema(response_put.json(), "put_user_response.json")
    UserAssertions.assert_put_user_response_body(response_put.json(), update_payload)

    user_api.delete_user(update_payload["username"])
