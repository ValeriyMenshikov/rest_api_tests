import allure
from requests import Response

from modules.http.dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, logic_provider):
        from generic import LogicProvider
        self.logic_provider: LogicProvider = logic_provider
        self.login_api = self.logic_provider.provider.http.dm_api_account.login_client

    def set_headers(self, headers) -> None:
        """Set the headers in class helper - Login"""
        self.login_api.client.session.headers.update(headers)

    def login_user(
            self,
            login: str,
            password: str,
            remember_me: bool = True
    ) -> Response:
        with allure.step('login_user'):
            response = self.login_api.post_v1_account_login(
                json=LoginCredentials(
                    login=login,
                    password=password,
                    remember_me=remember_me,
                )
            )
        return response

    def get_auth_token(self, login: str, password: str, remember_me: bool = True) -> dict:
        with allure.step('get_auth_token'):
            result = self.login_user(login=login, password=password, remember_me=remember_me)
            return {'X-Dm-Auth-Token': result.headers['X-Dm-Auth-Token']}

    def logout_user(self, **kwargs) -> Response:
        with allure.step('logout_user'):
            return self.login_api.del_v1_account_login(**kwargs)

    def logout_user_from_every_device(self, **kwargs) -> Response:
        with allure.step('logout_user_everywhere'):
            return self.login_api.del_v1_account_all(**kwargs)
