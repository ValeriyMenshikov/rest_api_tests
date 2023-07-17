from generic.helpers.account import Account
from generic.helpers.login import Login
from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi


class Facade:
    def __init__(self, host, mailhog=None, headers=None):
        self.login_api = LoginApi(host, headers)
        self.account_api = AccountApi(host, headers)
        self.mailhog = mailhog
        self.account = Account(self)
        self.login = Login(self)
