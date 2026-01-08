import allure
from api.json_schemas.validators import SchemaValidator


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
