import json
import time
from dataclasses import dataclass
from enum import Enum, auto
from time import sleep
from requests import Response
from common.restclient import Restclient


@dataclass
class EmailBodyInfo:
    token_name: str
    link_type: str


# class TokenType(Enum):
#     RESET_PASSWORD = auto()
#     ACTIVATE = auto()

class TokenType(Enum):
    RESET_PASSWORD = "reset"
    ACTIVATE = "activate"


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
        response = self.client.get(
            path="/api/v2/messages",
            params={
                'limit': limit
            }
        )

        return response

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from last email
        :return:
        """
        sleep(2)
        emails = self.get_api_v2_messages(limit=1).json()
        token_url = json.loads(emails["items"][0]["Content"]["Body"])["ConfirmationLinkUrl"]
        token = token_url.split("/")[-1]
        return token

    @staticmethod
    def _get_token_info_by_type(token_type: TokenType) -> EmailBodyInfo:
        match token_type:
            case token_type.RESET_PASSWORD:
                return EmailBodyInfo(token_name="password", link_type="ConfirmationLinkUri")
            case token_type.ACTIVATE:
                return EmailBodyInfo(token_name="activate", link_type="ConfirmationLinkUrl")

    # def get_token_by_login(self, login: str, token_type: TokenType, attempt: int = 5) -> str:
    #     token_info = self._get_token_info_by_type(token_type)
    #     if attempt == 0:
    #         raise AssertionError(f"Не удалось получить письмо с логином {login}")
    #     emails = self.get_api_v2_messages(limit=100).json()["items"]
    #     for email in emails:
    #         user_data = json.loads(email["Content"]["Body"])
    #         if token_info.link_type in user_data:
    #             confirmation_link_url = user_data[token_info.link_type]
    #             if login == user_data.get("Login") and token_info.token_name in confirmation_link_url:
    #                 token = confirmation_link_url.split("/")[-1]
    #                 return token
    #     time.sleep(2)
    #     return self.get_token_by_login(login=login, token_type=token_type, attempt=attempt - 1)

    def get_token_by_login(self, login: str, token_type: TokenType = TokenType.ACTIVATE, attempt: int = 5) -> str:
        """
        Метод получения токена
        :param login:
        :param token_type: activate or reset
        :param attempt:
        :return:
        """
        if token_type.value == 'activate':
            link_type = "ConfirmationLinkUrl"
        elif token_type.value == 'reset':
            link_type = "ConfirmationLinkUri"
        else:
            raise AssertionError(f'token_type should be activate or reset, but token_type == {token_type}')

        if attempt == 0:
            raise AssertionError(f"Не удалось получить письмо с логином {login}")
        emails = self.get_api_v2_messages(limit=100).json()["items"]
        for email in emails:
            user_data = json.loads(email["Content"]["Body"])
            if user_data.get('Login') == login and user_data.get(link_type):
                token_link_url = user_data[link_type]
                token = token_link_url.split("/")[-1]
                return token
        time.sleep(2)
        return self.get_token_by_login(login=login, token_type=token_type, attempt=attempt - 1)

    def delete_all_messages(self) -> Response:
        response = self.client.delete(path="/api/v1/messages")
        return response
