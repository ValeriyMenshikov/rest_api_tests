from generic.helpers.account import Account
from generic.helpers.login import Login
from modules.http.dm_api_account.apis import LoginApi, AccountApi


class LogicProvider:
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
