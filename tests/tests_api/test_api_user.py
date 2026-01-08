import allure
from data.generators import generate_update_payload
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


@allure.epic("выход из системы")
@allure.title("успешный разлогин пользователя")
@allure.severity(allure.severity_level.NORMAL)
def test_get_logout_success(user_api, headers):

    get_response = user_api.get_user_logout()

    assert get_response.status_code == 200
    SchemaValidator.validate_schema(get_response.json(), "responses/get_logout_response.json")

    response_body = get_response.json()
    assert response_body["code"] == 200
    assert response_body["type"] == "unknown"
    assert response_body["message"] == "ok"


@allure.epic("создание пользователя")
@allure.title("успешное создание пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_post_create_user_success(user_api, headers, user_payload):

    SchemaValidator.validate_schema(
        data_to_validate=user_payload, schema_filename="requests/post_create_user_payload.json"
    )

    create_response = user_api.post_create_user_request_body(user_payload)
    assert create_response.status_code == 200

    SchemaValidator.validate_schema(
        create_response.json(), "responses/post_create_user_response.json"
    )

    response_body = create_response.json()
    expected_message = str(user_payload["id"])
    assert response_body["code"] == 200
    assert response_body["type"] == "unknown"
    assert response_body["message"] == expected_message

    username = user_payload["username"]

    user_api.delete_user(username)


@allure.epic("получение пользователя")
@allure.title("успешное получение пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_user_by_user_name_success(user_api, headers, user_payload):

    user_api.post_create_user_request_body(user_payload)

    username = user_payload["username"]

    get_response = user_api.get_user_by_username(username)

    assert get_response.status_code == 200
    SchemaValidator.validate_schema(get_response.json(), "responses/get_user_response.json")
    UserAssertions.assert_get_user_response_body(get_response.json(), user_payload)

    user_api.delete_user(username)


@allure.epic("обновление пользователя")
@allure.title("успешное обновление пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_put_update_user_success(user_api, headers, user_payload):

    user_api.post_create_user_request_body(user_payload)

    old_username = user_payload["username"]

    update_payload = generate_update_payload(user_payload)

    SchemaValidator.validate_schema(
        data_to_validate=update_payload, schema_filename="requests/put_user_payload.json"
    )

    response_put = user_api.put_update_user_request_body(old_username, update_payload)

    assert response_put.status_code == 200

    SchemaValidator.validate_schema(response_put.json(), "responses/put_user_response.json")
    UserAssertions.assert_put_user_response_body(response_put.json(), update_payload)

    user_api.delete_user(update_payload["username"])


@allure.epic("удаление пользователя")
@allure.title("успешное удаление пользователя")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_user_success(user_api, headers, user_payload):

    user_api.post_create_user_request_body(user_payload)

    username = user_payload["username"]

    delete_response = user_api.delete_user(username)
    assert delete_response.status_code == 200

    SchemaValidator.validate_schema(delete_response.json(), "responses/delete_user_response.json")

    response_body = delete_response.json()
    assert response_body["code"] == 200
    assert response_body["type"] == "unknown"
    assert response_body["message"] == username

    get_response = user_api.get_user_by_username(username)
    assert get_response.status_code == 404