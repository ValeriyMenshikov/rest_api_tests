import pprint
import pytest
from betterproto import Casing
from apis.dm_api_search_async import SearchRequest, SearchEntityType


def test_search(grpc_search):
    response = grpc_search.search(
        query='test_post',
        skip=0,
        size=10,
        search_across=['FORUM_TOPIC']
    )


@pytest.mark.asyncio
async def test_search_async(grpc_search_async):
    response = await grpc_search_async.search(
        search_request=SearchRequest(
            query='test_post',
            skip=0,
            size=10,
            search_across=[SearchEntityType.FORUM_TOPIC]
        )
    )
    pprint.pprint(response.to_dict(casing=Casing.SNAKE))
