from tests.api.pages.user_api import User


def test_get_login_user_success(common_username,common_password,user_payload,api_url,headers):

    user = User(api_url,headers)

    user.post_create_user_request_body(user_payload)

    response_get = user.get_user_login(common_username,common_password)
    assert response_get.status_code == 200
    user.validate_get_user_login_response()







