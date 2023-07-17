import json

import allure
from requests import Response
from restclient.restclient import Restclient
import structlog
import time

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def decorator(fn):
    def wrapper(*args, **kwargs):
        for i in range(5):
            response = fn(*args, **kwargs)
            emails = response.json()['items']
            if len(emails) < 5:
                print(f'attempt{i}')
                time.sleep(2)
                continue
            else:
                return response

    return wrapper


class MailhogApi:

    def __init__(self, host):
        self.host = host
        self.client = Restclient(host=host)

    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        with allure.step('получаем сообщения'):
            response = self.client.get(
                path=f"/api/v2/messages",
                params={
                    'limit': limit
                }
            )

        return response

    def get_token_from_last_email(self, token_type: str = 'password') -> str:
        """
        Get user activation token from last email
        Метод может принять два параметра
        1)password для получения токена для сброса пароля - установлен по умолчанию
        2)activate для получения токена для активации пользователя нужно передавать в вызове функции
        :return:
        """
        with allure.step('получаем токен из последнего сообщения'):
            emails = self.get_api_v2_messages(limit=1).json()
            if token_type == 'password':
                token_url = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUri']
            elif token_type == 'activate':
                token_url = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUrl']
            token = token_url.split('/')[-1]
        return token

    def get_token_by_login(self, login: str, attempt=5):
        if attempt == 0:
            raise AssertionError(f'Не получили письмо с логином {login}')
        with allure.step('Получаем токен по логину'):
            emails = self.get_api_v2_messages(limit=100).json()['items']
            for email in emails:
                user_data = json.loads(email['Content']['Body'])
                if login == user_data.get('Login'):
                    token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                    return token
            time.sleep(2)
        return self.get_token_by_login(login=login, attempt=attempt - 1)

    def delete_all_messages(self):
        with allure.step('Удаляем все сообщения'):
            response = self.client.delete(path='/api/v1/messages')
        return response
