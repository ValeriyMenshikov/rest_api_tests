from generic.helpers.account import Account
from generic.helpers.login import Login
from apis.dm_api_account.apis.account_api import AccountApi
from apis.dm_api_account.apis.login_api import LoginApi


class Facade:
    def __init__(self, host, mailhog=None, headers=None, disable_log=False):
        self.login_api = LoginApi(host, headers, disable_log=disable_log)
        self.account_api = AccountApi(host, headers, disable_log=disable_log)
        self.mailhog = mailhog
        self.mailhog.client.disable_log = disable_log
        self.account = Account(self)
        self.login = Login(self)

    def set_headers(self, headers):
        self.login.set_headers(headers)
        self.account.set_headers(headers)
