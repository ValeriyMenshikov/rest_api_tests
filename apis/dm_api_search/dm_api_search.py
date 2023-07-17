import grpc
import structlog
import uuid

from google.protobuf.json_format import MessageToDict

from apis.dm_api_search.search_pb2 import SearchRequest
from apis.dm_api_search.search_pb2_grpc import SearchEngineStub


def grpc_loging(func):
    def wrapper(self, request, *args, **kwargs):
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        method = func.__name__
        log.msg(
            event='request',
            method=method,
            channel=self.target,
            request=MessageToDict(request)
        )
        try:
            response = func(self, request, *args, **kwargs)
            log.msg(
                event='response',
                response=MessageToDict(response)
            )
            return response
        except Exception as e:
            print(f"error {e}")
            raise

    return wrapper


class DmApiSearch:
    def __init__(self, target):
        self.target = target
        self.channel = grpc.insecure_channel(target=self.target)
        self.client = SearchEngineStub(channel=self.channel)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='grpc')

    @grpc_loging
    def search(self, request: SearchRequest):
        response = self.client.Search(request=request)
        return response

    def close(self):
        self.channel.close()