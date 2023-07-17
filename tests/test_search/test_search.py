import pytest

from apis.dm_api_search_async import SearchRequest, SearchEntityType


def test_search(grpc_search):
    response = grpc_search.search(
        query="testplease",
        size=1,
        skip=0,
        search_across=['FORUM_TOPIC']
    )


@pytest.mark.asyncio
async def test_search_async(grpc_search_async):
    response = await grpc_search_async.search(
        search_request=SearchRequest(
            query="testplease",
            size=1,
            skip=0,
            search_across=[SearchEntityType.FORUM_TOPIC]
        )
    )

    print(response.to_dict())
