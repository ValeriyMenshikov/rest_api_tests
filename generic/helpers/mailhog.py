import json
from enum import Enum
from time import sleep
from dataclasses import dataclass


@dataclass
class EmailBodyInfo:
    token_name: str
    link_type: str


class TokenType(str, Enum):
    RESET_PASSWORD = "reset"
    ACTIVATE = "activate"


class MailHog:
    def __init__(self, logic_provider):
        from generic import LogicProvider

        self.logic_provider: LogicProvider = logic_provider
        self.mailhog = self.logic_provider.provider.http.mailhog

    @staticmethod
    def _get_token_info_by_type(token_type: TokenType) -> EmailBodyInfo:
        if token_type == TokenType.RESET_PASSWORD:
            return EmailBodyInfo(token_name="password", link_type="ConfirmationLinkUri")
        elif token_type == TokenType.ACTIVATE:
            return EmailBodyInfo(token_name="activate", link_type="ConfirmationLinkUrl")

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from last email
        :return:
        """
        sleep(2)
        emails = self.mailhog.get_api_v2_messages(limit=1).json()
        token_url = json.loads(emails["items"][0]["Content"]["Body"])[
            "ConfirmationLinkUrl"
        ]
        token = token_url.split("/")[-1]
        return token

    def get_token_by_login(
        self, login: str, token_type: TokenType = TokenType.ACTIVATE, attempt: int = 5
    ) -> str:
        """
        Method to retrieve a token by login.

        Args:
            login (str): The user's login.
            token_type (TokenType): The type of token (activate or reset).
            attempt (int): The number of attempts to retrieve the token.

        Returns:
            str: The token associated with the login.
        """
        # Determine the link type based on token type
        if token_type == TokenType.ACTIVATE:
            link_type = "ConfirmationLinkUrl"
        elif token_type == TokenType.RESET_PASSWORD:
            link_type = "ConfirmationLinkUri"
        else:
            raise AssertionError(
                f"token_type should be activate or reset, but token_type == {token_type}"
            )

        # Check for valid attempts
        if attempt == 0:
            raise AssertionError(f"Failed to receive email with login {login}")

        # Retrieve emails and search for the token
        emails = self.mailhog.get_api_v2_messages(limit=100).json()["items"]
        for email in emails:
            user_data = json.loads(email["Content"]["Body"])
            if user_data.get("Login") == login and user_data.get(link_type):
                token_link_url = user_data[link_type]
                token = token_link_url.split("/")[-1]
                return token

        # Retry if token not found after waiting
        sleep(2)
        return self.get_token_by_login(
            login=login, token_type=token_type, attempt=attempt - 1
        )
