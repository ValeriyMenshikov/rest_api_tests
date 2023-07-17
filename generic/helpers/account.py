import allure

from dm_api_account.models import Registration, ResetPassword, ChangeEmail, ChangePassword


class Account:
    def __init__(self, facade):
        self.facade = facade

    def set_headers(self, headers):
        """Set the headers in class helper - Account"""
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str, status_code: int = 201):
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

    def activate_registered_user(self, login: str):
        with allure.step('activate_registered_user'):
            token = self.facade.mailhog.get_token_by_login(login=login)
            response = self.facade.account_api.put_v1_account_token(
                token=token
            )
        return response

    def get_current_user(self, **kwargs):
        with allure.step('get_current_user'):
            return self.facade.account_api.get_v1_account(**kwargs)

    def reset_user_password(self, login: str, email: str):
        with allure.step('reset_user_password'):
            response = self.facade.account_api.post_v1_account_password(
                json=ResetPassword(
                    login=login,
                    email=email
                )
            )
        return response

    def change_user_email(self, login: str, password: str, email: str, status_code: int = 200):
        with allure.step('change_user_email'):
            response = self.facade.account_api.put_v1_account_email(
                json=ChangeEmail(
                    login=login,
                    password=password,
                    email=email
                ),
                status_code=status_code
            )
        return response

    def change_user_password(self, login: str, password: str, new_password: str, token: str, status_code: int = 200):
        with allure.step('change_user_email'):
            response = self.facade.account_api.put_v1_account_password(
                json=ChangePassword(
                    login=login,
                    token=token,
                    oldPassword=password,
                    newPassword=new_password,
                ),
                status_code=status_code
            )
        return response
