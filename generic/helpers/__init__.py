from generic.helpers.account import Account
from generic.helpers.login import Login


class LogicProvider:
    def __init__(self, login_api, account_api, mailhog_api):
        self.login_api = login_api
        self.account_api = account_api
        self.mailhog = mailhog_api
        self.account = Account(self)
        self.login = Login(self)

    def set_headers(self, headers):
        self.login.set_headers(headers)
        self.account.set_headers(headers)
