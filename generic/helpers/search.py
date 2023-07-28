from modules.grpc.dm_api_search.dm_api_search import DmApiSearch
from modules.grpc.dm_api_search.search_pb2 import SearchRequest, SearchResponse


class Search:

    def __init__(self, target) -> None:
        self.grpc_search = DmApiSearch(target=target)

    def search(self, query: str, skip: int, size: int, search_across: list) -> SearchResponse:
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
