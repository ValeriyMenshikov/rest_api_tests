import allure
from requests import Response
from modules.http.dm_api_account.models import (
    Registration,
    ResetPassword,
    ChangeEmail,
    ChangePassword,
    UserEnvelope,
    UserDetailsEnvelope
)
from modules.http.mailhog.mailhog import TokenType


class Account:
    def __init__(self, facade):
        from generic.helpers import LogicProvider
        self.facade: LogicProvider = facade

    def set_headers(self, headers):
        """Set the headers in class helper - Account"""
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(
            self,
            login: str,
            email: str,
            password: str,
            status_code: int = 201
    ) -> Response:
        with allure.step('registration new user'):
            response = self.facade.account_api.post_v1_account(
                status_code=status_code,
                json=Registration(
                    login=login,
                    email=email,
                    password=password
                )
            )
        return response

    def activate_registered_user(
            self,
            login: str,
            token_type: TokenType = TokenType.ACTIVATE
    ) -> UserEnvelope:
        with allure.step('activate_registered_user'):
            token = self.facade.mailhog.get_token_by_login(login=login, token_type=token_type)
            response = self.facade.account_api.put_v1_account_token(
                token=token
            )
        return response

    def get_current_user(self, **kwargs) -> UserDetailsEnvelope | Response:
        with allure.step('get_current_user'):
            return self.facade.account_api.get_v1_account(**kwargs)

    def reset_user_password(
            self,
            login: str,
            email: str
    ) -> UserEnvelope | Response:
        with allure.step('reset_user_password'):
            response = self.facade.account_api.post_v1_account_password(
                json=ResetPassword(
                    login=login,
                    email=email
                )
            )
        return response

    def change_user_email(
            self,
            login: str,
            password: str,
            email: str
    ) -> UserEnvelope | Response:
        with allure.step('change_user_email'):
            response = self.facade.account_api.put_v1_account_email(
                json=ChangeEmail(
                    login=login,
                    password=password,
                    email=email
                )
            )
        return response

    def change_user_password(
            self,
            login: str,
            password: str,
            new_password: str,
            token: str
    ) -> UserEnvelope | Response:
        with allure.step('change_user_email'):
            response = self.facade.account_api.put_v1_account_password(
                json=ChangePassword(
                    login=login,
                    token=token,
                    oldPassword=password,
                    newPassword=new_password,
                )
            )
        return response
