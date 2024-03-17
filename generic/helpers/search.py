from modules.grpc.dm_api_search.search_pb2 import SearchRequest, SearchResponse


class Search:
    def __init__(self, logic_provider):
        from generic import LogicProvider

        self.logic_provider: LogicProvider = logic_provider
        self.grpc_search = self.logic_provider.provider.grpc.dm_api_search

    def search(
        self,
        query: str,
        skip: int,
        size: int,
        search_across: list,
    ) -> SearchResponse:
        response = self.grpc_search.search(
            request=SearchRequest(
                query=query,
                size=size,
                skip=skip,
                searchAcross=search_across,
            ),
        )
        return response

    # def close(self):
    #     self.grpc_search.close()
