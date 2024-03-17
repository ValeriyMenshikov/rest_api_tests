from functools import cached_property
from modules.http.mailhog.client import MailhogApi
from modules.http.dm_api_account.stubs import DmApiAccountHTTPStubs
from vyper import v


class HTTPConnector:
    @cached_property
    def mailhog(self) -> MailhogApi:
        return MailhogApi(host=v.get("service.mailhog"))

    @cached_property
    def dm_api_account(self) -> DmApiAccountHTTPStubs:
        return DmApiAccountHTTPStubs(host=v.get("service.dm_api_account"))
