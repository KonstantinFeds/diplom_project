from tests.api.pages.user_api import User
from tests.api.data.generators import payload_generate_user


def test_put_update_user_success(api_url,headers,user_payload,common_username):

    user = User(api_url, headers)

    #создаем нового user
    user.post_create_user_request_body(user_payload)


    #генерим данные для нового
    user.generate_update_payload(user_payload)

    #Обновляем use
    user.validate_put_user_payload(user.update_payload)
    response_put = user.put_update_user_request_body(common_username, user.update_payload)

    assert response_put.status_code == 200
    user.validate_put_user_response()
    user.assert_put_user_response_body(user_payload)

    user.get_user_by_username(user.new_username)
    user.assert_get_response_body(user.update_payload)


    response_data = user.response.json()
    assert response_data['id'] == user_payload['id']


    user.delete_user(user.new_username)


