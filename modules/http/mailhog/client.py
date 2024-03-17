from requests import Response
from common.restclient import Restclient


class MailhogApi:
    def __init__(self, host: str = "http://localhost:5025", disable_log=False) -> None:
        self.host = host
        self.disable_log = disable_log
        self.client = Restclient(host=host, disable_log=self.disable_log)

    # @decorator
    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        response = self.client.get(path="/api/v2/messages", params={"limit": limit})

        return response

    def delete_all_messages(self) -> Response:
        response = self.client.delete(path="/api/v1/messages")
        return response
