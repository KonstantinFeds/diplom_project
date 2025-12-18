import json
import requests
from jsonschema import validate
from conftest import user_payload
from tests.api.data.generators import payload_generate_user
from utils.file import path_from_json_schemas



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


        return self.response


    def validate_post_create_user_response(self):

        with open(path_from_json_schemas("post_create_user.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)


    def get_user_by_username(self,common_username):

        self.response = requests.request(method='GET',
                                    url=f'{self.api_url}/v2/user/{common_username}',
                                    headers=self.headers,
                                    timeout=10
                                    )


        return self.response

    def validate_get_user_response(self):
        with open(path_from_json_schemas("get_user.json"), encoding="utf-8") as file:
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

        return  self.response

    def validate_put_user_response(self):
        with open(path_from_json_schemas("put_user.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)


    def generate_update_payload(self,original_payload):
        self.update_payload = payload_generate_user()
        self.update_payload["id"] = original_payload["id"]
        self.new_username = self.update_payload["username"]


    def get_user_login(self,common_username, common_password):
        self.response = requests.request(method='GET',
                                         url=f'{self.api_url}/v2/user/login',
                                         headers=self.headers,
                                         params={
                                             'username': common_username,
                                            'password': common_password
                                         },
                                         timeout=10)

        return self.response


    def validate_get_user_login_response(self):
        with open(path_from_json_schemas("get_login_user.json"), encoding="utf-8") as file:
            schema = json.load(file)
            validate(self.response.json(), schema)









