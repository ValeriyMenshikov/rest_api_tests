from apis.dm_api_account.models import Registration


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str, status_code: int = 201):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password,
            ),
            status_code=status_code
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response
