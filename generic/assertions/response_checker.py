import json
import allure
import requests
from contextlib import contextmanager
from hamcrest import assert_that, has_entries


@contextmanager
def check_status_code_http(expected_status_code: requests.codes = requests.codes.OK,
                           expected_result: dict = {}):
    from dm_api_account import ApiException
    with allure.step('Check HTTP status code'):
        try:
            yield
        except ApiException as e:
            assert e.status == expected_status_code
            assert_that(json.loads(e.body)['errors'], has_entries(expected_result))
