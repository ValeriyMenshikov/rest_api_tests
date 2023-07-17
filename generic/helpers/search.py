from apis.dm_api_search.dm_api_search import DmApiSearch
from apis.dm_api_search.search_pb2 import SearchRequest


class Search:

    def __init__(self, target):
        self.grpc_search = DmApiSearch(target=target)

    def search(self, query: str, skip: int, size: int, search_across: list):
        response = self.grpc_search.search(
            request=SearchRequest(
                query=query,
                size=size,
                skip=skip,
                searchAcross=search_across
            )
        )
        return response

    # def close(self):
    #     self.grpc_search.close()
