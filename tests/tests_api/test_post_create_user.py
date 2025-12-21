
from tests.api.pages.user_api import User


def test_post_create_user_success(api_url,headers,user_payload,common_username):

    user = User(api_url,headers)

    user.validate_post_create_user_payload(user_payload)
    create_response = user.post_create_user_request_body(user_payload)
    assert create_response.status_code == 200

    user.validate_post_create_user_response()
    user.assert_post_create_response_body(user_payload)

    user.delete_user(common_username)

