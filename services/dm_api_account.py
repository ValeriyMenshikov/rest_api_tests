from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi


class DmApiAccount:
    def __init__(self, host, headers=None):
        self.account = AccountApi(host, headers)
        self.login = LoginApi(host, headers)
