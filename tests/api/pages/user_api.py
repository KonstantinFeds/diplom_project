import json
import requests
from jsonschema import validate
from conftest import user_payload, common_username
from tests.api.data.generators import payload_generate_user
from utils.file import path_from_json_schemas
from utils.logger import response_logging, response_attaching



class User:

    def __init__(self,api_url, headers):
        self.response = None
        self.api_url = api_url
        self.headers = headers
        self.update_payload = None
        self.new_username = None



    def post_create_user_request_body(self,user_payload):

        self.response = requests.request(method='POST',
                                url=f'{self.api_url}/v2/user/',
                                headers=self.headers,
                                json=user_payload,
                                timeout=10)

        response_logging(self.response)
        response_attaching(self.response)

        return self.response



    def validate_post_create_user_payload(self, user_payload):

        with open(path_from_json_schemas('post_create_user_payload.json'), encoding="utf-8") as file:
            schema = json.load(file)
            validate(user_payload, schema)

        return self

    def validate_post_create_user_response(self):

        with open(path_from_json_schemas("post_create_user_response.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)


    def assert_post_create_response_body(self,user_payload):

        response_body = self.response.json()
        expected_message = str(user_payload["id"])

        assert (response_body["code"] == 200 and
                response_body["type"] == "unknown" and
                response_body["message"] == expected_message)


    def get_user_by_username(self,common_username):

        self.response = requests.request(method='GET',
                                    url=f'{self.api_url}/v2/user/{common_username}',
                                    headers=self.headers,
                                    timeout=10
                                    )

        response_logging(self.response)
        response_attaching(self.response)


        return self.response

    def validate_get_user_response(self):
        with open(path_from_json_schemas("get_user_response.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)


    def assert_get_response_body(self, payload):

        response_body = self.response.json()
        expected_result = ['id',
                           'username',
                           'firstName',
                           'lastName',
                           'email',
                           'password',
                           'phone',
                           'userStatus']
        for key in expected_result:
            assert response_body[key] == payload[key], f"Не совпадает значение ключа: {key}"


    def put_update_user_request_body(self,common_username,user_payload):
        self.response = requests.request(method='PUT',
                                         url=f'{self.api_url}/v2/user/{common_username}',
                                         headers=self.headers,
                                         json=user_payload,
                                         timeout=10)

        response_logging(self.response)
        response_attaching(self.response)

        return  self.response


    def generate_update_payload(self,original_payload):
        self.update_payload = payload_generate_user()
        self.update_payload["id"] = original_payload["id"]
        self.new_username = self.update_payload["username"]


    def validate_put_user_payload(self,update_payload):
        with open(path_from_json_schemas('put_user_payload.json'), encoding="utf-8") as file:
            schema = json.load(file)
            validate(update_payload, schema)

        return self



    def validate_put_user_response(self):
        with open(path_from_json_schemas("put_user_response.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)


    def assert_put_user_response_body(self,user_payload):

        response_body = self.response.json()
        expected_message = str(user_payload["id"])

        assert (response_body["code"] == 200 and
                response_body["type"] == "unknown" and
                response_body["message"] == expected_message)


    def get_user_login(self,common_username, common_password):
        self.response = requests.request(method='GET',
                                         url=f'{self.api_url}/v2/user/login',
                                         headers=self.headers,
                                         params={
                                             'username': common_username,
                                            'password': common_password
                                         },
                                         timeout=10)
        response_logging(self.response)
        response_attaching(self.response)

        return self.response


    def validate_get_user_login_response(self):
        with open(path_from_json_schemas("get_login_response.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)

    def assert_get_user_login_response_body(self):

        response_body = self.response.json()
        message = response_body['message']
        session_id = message.split(":")[-1]

        assert (response_body['code'] == 200 and
                response_body['type'] == 'unknown' and
                response_body['message'] == f'logged in user session:{session_id}' and
                len(session_id) == 13)


    def get_user_logout(self):
        self.response = requests.request(method='GET',
                                         url=f'{self.api_url}/v2/user/logout',
                                         headers=self.headers,
                                         timeout=10)
        response_logging(self.response)
        response_attaching(self.response)

        return self.response

    def validate_get_user_logout_response(self):
        with open(path_from_json_schemas("get_logout_response.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)

    def assert_get_user_logout_response_body(self):

        response_body = self.response.json()

        assert (response_body['code'] == 200 and
                response_body['type'] == 'unknown' and
                response_body['message'] == 'ok')




    def delete_user(self, common_username):
        self.response = requests.request(method='DELETE',
                                         url=f'{self.api_url}/v2/user/{common_username}',
                                         headers=self.headers,
                                         timeout=10)

        response_logging(self.response)
        response_attaching(self.response)

        return self.response

    def validate_delete_user_response(self):
        with open(path_from_json_schemas("delete_user_response.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)


    def assert_delete_user_response_body(self,common_user_name):

        response_body = self.response.json()

        assert (response_body['code'] == 200 and
                response_body['type'] == 'unknown' and
                response_body['message'] == common_user_name)













