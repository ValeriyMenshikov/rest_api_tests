from modules.http import HTTPConnector
from modules.db import DBConnector
from modules.grpc import GRPCConnector


class _Provider:
    http = HTTPConnector()
    db = DBConnector()
    grpc = GRPCConnector()


modules_provider = _Provider
