import requests
from requests import Response
from ..models.registration_model import registration_model
from ..models.reset_password_model import reset_password_model
from ..models.change_email_model import change_email_model
from ..models.change_password_model import change_password_model
from requests import session


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        Register new user
        :param json: registration_model
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        Reset registered user password
        :param json: reset_password_model
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_email(self, json: change_email_model, **kwargs) -> Response:
        """
        Change registered user email
        :param json: change_email_model
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: change_password_model, **kwargs) -> Response:
        """
        Change registered user password
        :param json: change_password_model
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        :param token:
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/{token}",
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.session.get(
            url=f"{self.host}/v1/account",
            **kwargs
        )
        return response
