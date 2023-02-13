from requests import Response
from dm_api_account.models import *
from dm_api_account.utilities import validate_request_json, check_status_code
from restclient.restclient import Restclient


# TODO добавить модели и обработку статус кодов

class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: Registration, status_code: int = 201, **kwargs) -> Response:
        """
        Register new user
        :param status_code:
        :param json: registration_model
        :return:
        """
        response = self.client.post(
            path=f"/v1/account",
            json=validate_request_json(json),
            **kwargs
        )
        check_status_code(response, status_code)
        return response

    def post_v1_account_password(self, json: ResetPassword, status_code: int = 200,
                                 **kwargs) -> Response | UserEnvelope:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """
        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        check_status_code(response, status_code)
        if status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmail, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: ChangePassword, **kwargs) -> Response:
        """
        Change registered user password
        :param json: change_password_model
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, status_code: int = 200, **kwargs) -> Response | UserEnvelope:
        """
        :param status_code:
        :param token:
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        if status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def get_v1_account(self, status_code: int = 200, **kwargs) -> Response | UserDetailsEnvelope:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        if status_code == 200:
            return UserDetailsEnvelope(**response.json())
        return response
