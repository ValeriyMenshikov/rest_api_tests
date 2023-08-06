from functools import cached_property
from modules.grpc.dm_api_search.dm_api_search import DmApiSearch
from vyper import v


class GRPCConnector:

    @cached_property
    def dm_api_search(self) -> DmApiSearch:
        return DmApiSearch(target=v.get('service.dm_api_search'))
