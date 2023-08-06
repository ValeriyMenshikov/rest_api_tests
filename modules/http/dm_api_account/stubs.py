from functools import cached_property


class DmApiAccountHTTPStubs:
    def __init__(self, host):
        self.host = host

    @cached_property
    def account_client(self):
        from modules.http.dm_api_account.apis import AccountApi
        return AccountApi(host=self.host)

    @cached_property
    def login_client(self):
        from modules.http.dm_api_account.apis import LoginApi
        return LoginApi(host=self.host)
