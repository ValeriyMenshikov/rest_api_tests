import allure
from requests import Response
from common_libs.restclient.restclient import Restclient
from apis.dm_api_account.models import *
from ..utilities import validate_request_json, validate_status_code


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(
            self,
            json: LoginCredentials,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        :param status_code:
        :param json: login_credentials
        Authenticate via credentials
        :return:
        """
        with allure.step('Аутентификация'):
            response = self.client.post(
                path=f"/v1/account/login",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            UserEnvelope(**response.json())
        return response

    def del_v1_account_all(self, status_code: int = 204, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """
        with allure.step('Выходим со всех устройств'):
            response = self.client.delete(
                path=f"/v1/account/login/all",
                **kwargs
            )
        validate_status_code(response, status_code)
        return response

    def del_v1_account_login(self, status_code: int = 204, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """

        with allure.step('Разлогиниваемся'):
            response = self.client.delete(
                path=f"/v1/account/login",
                **kwargs
            )
        validate_status_code(response, status_code)
        return response
