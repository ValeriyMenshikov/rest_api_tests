import allure
from requests import Response
from common_libs.restclient.restclient import Restclient
from apis.dm_api_account.utilities import validate_request_json, validate_status_code
from apis.dm_api_account.models import *


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(
            self,
            json: Registration,
            status_code: int = 201,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        :param status_code:
        :param json: registration_model
        Register new user
        :return:
        """
        with allure.step('Регистрация нового пользователя'):
            response = self.client.post(
                path=f"/v1/account",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)
        return response

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserDetailsEnvelope:
        """
        Get current user
        :return:
        """
        with allure.step('Получаем текущего пользователя'):
            response = self.client.get(
                path=f"/v1/account",
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserDetailsEnvelope(**response.json())
        return response

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        :param status_code:
        :param token: str
        Activate registered user
        :return:
        """
        with allure.step('Активируем зарегистрированного пользователя'):
            response = self.client.put(
                path=f"/v1/account/{token}",
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | BadRequestError | Response:
        """
        :param status_code:
        :param json: reset_password
        Reset registered user password
        :return:
        """
        with allure.step('Сбрасываем пароль'):
            response = self.client.post(
                path=f"/v1/account/password",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 201:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        :param status_code:
        :param json: change_password
        Change registered user password
        :return:
        """
        with allure.step('Меняем пароль'):
            response = self.client.put(
                path=f"/v1/account/password",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelope | Response:
        """
        :param status_code:
        :param json: change_email
        Change registered user email
        :return:
        """
        with allure.step('Меняем емейл'):
            response = self.client.put(
                path=f"/v1/account/email",
                json=validate_request_json(json),
                **kwargs
            )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response
