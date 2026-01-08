import allure


class UserAssertions:

    @staticmethod
    @allure.step("Проверка ответа получения пользователя")
    def assert_get_user_response_body(response_body: dict, expected_payload: dict):
        for key in expected_payload.keys():
            if key in response_body:
                assert (
                    response_body[key] == expected_payload[key]
                ), f"Не совпадает значение ключа: {key}"

    @staticmethod
    @allure.step("Проверка ответа обновления пользователя")
    def assert_put_user_response_body(response_body: dict, user_payload: dict):
        expected_message = str(user_payload["id"])
        assert (
            response_body["code"] == 200
            and response_body["type"] == "unknown"
            and response_body["message"] == expected_message
        )

    @staticmethod
    @allure.step("Проверка ответа логина пользователя")
    def assert_get_user_login_response_body(response_body: dict):
        message = response_body["message"]
        session_id = message.split(":")[-1]

        assert (
            response_body["code"] == 200
            and response_body["type"] == "unknown"
            and response_body["message"] == f"logged in user session:{session_id}"
            and len(session_id) == 13
        )
