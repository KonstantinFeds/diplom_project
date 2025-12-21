from tests.api.pages.user_api import User


def test_delete_user_success(api_url,headers,common_username,user_payload):

    user = User(api_url,headers)

    user.post_create_user_request_body(user_payload)

    delete_response = user.delete_user(common_username)
    assert delete_response.status_code == 200

    user.validate_delete_user_response()
    user.assert_delete_user_response_body(common_username)

    get_response = user.get_user_by_username(common_username)
    assert get_response.status_code == 404
