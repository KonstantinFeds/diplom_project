from tests.api.pages.user_api import User


def test_get_logout_success(api_url,headers):
    user = User(api_url,headers)


    get_response = user.get_user_logout()

    assert get_response.status_code == 200
    user.validate_get_user_logout_response()
    user.assert_get_user_logout_response_body()



