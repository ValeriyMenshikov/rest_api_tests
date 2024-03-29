from functools import cached_property

from grpclib.client import Channel
from modules.grpc.dm_api_account import AccountServiceStub
from modules.grpc.dm_api_search.dm_api_search import DmApiSearch
from vyper import v


class GRPCConnector:
    @cached_property
    def dm_api_search(self) -> DmApiSearch:
        return DmApiSearch(target=v.get("service.dm_api_search"))

    @cached_property
    def dm_api_account(self) -> AccountServiceStub:
        channel = Channel(host=v.get("service.dm_api_account_grpc"), port=5055)
        return AccountServiceStub(channel=channel)
