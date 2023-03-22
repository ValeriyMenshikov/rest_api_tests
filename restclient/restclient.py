import requests.exceptions
from requests import session, Response
import structlog
import uuid
import curlify
import allure
import json


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        body = kwargs.get('json')
        if body:
            allure.attach(
                json.dumps(kwargs.get('json'), indent=2),
                name='request',
                attachment_type=allure.attachment_type.JSON
            )
        response = fn(*args, **kwargs)
        try:
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            response_text = response.text
            status_code = f'< status_code {response.status_code} >'
            allure.attach(
                response_text if len(response_text) > 0 else status_code,
                name='response',
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                json.dumps(response_json, indent=2),
                name='response',
                attachment_type=allure.attachment_type.JSON
            )
        return response

    return wrapper


class Restclient:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')

    @allure_attach
    def post(self, path: str, **kwargs) -> Response:
        return self._send_request('POST', path, **kwargs)

    @allure_attach
    def get(self, path: str, **kwargs) -> Response:
        return self._send_request('GET', path, **kwargs)

    @allure_attach
    def put(self, path: str, **kwargs) -> Response:
        return self._send_request('PUT', path, **kwargs)

    @allure_attach
    def patch(self, path: str, **kwargs) -> Response:
        return self._send_request('PATCH', path, **kwargs)

    @allure_attach
    def delete(self, path: str, **kwargs) -> Response:
        return self._send_request('DELETE', path, **kwargs)

    def _send_request(self, method, path, **kwargs):
        full_url = self.host + path
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            method=method,
            full_url=full_url,
            params=kwargs.get('params'),
            headers=kwargs.get('headers'),
            json=kwargs.get('json'),
            data=kwargs.get('data')
        )
        response = self.session.request(
            method=method,
            url=full_url,
            **kwargs
        )
        curl = curlify.to_curl(response.request)
        allure.attach(
            curl,
            name='curl',
            attachment_type=allure.attachment_type.TEXT
        )
        print(curl)
        log.msg(
            event='response',
            status_code=response.status_code,
            headers=response.headers,
            json=self._get_json(response),
            text=response.text,
            content=response.content,
            curl=curl
        )
        return response

    @staticmethod
    def _get_json(response):
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return
