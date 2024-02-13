from collections import namedtuple
import pytest
import structlog
from vyper import v
from pathlib import Path
from generic import LogicProvider
from data.post_v1_account import PostV1AccountData as user_data
import os

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

options = (
    'service.dm_api_account',
    'service.mailhog',
    'database.dm3_5.host'
    'disable_log',
    'telegram.chat_id',
    'telegram.token',
)


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))
    os.environ['TELEGRAM_BOT_CHAT_ID'] = v.get('telegram.chat_id')
    os.environ['TELEGRAM_BOT_ACCESS_TOKEN'] = v.get('telegram.token')


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='prod')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)


@pytest.fixture
def prepare_user(logic):
    user_tuple = namedtuple('User', 'login, email, password, new_password')
    user = user_tuple(
        login=user_data.login,
        password=user_data.password,
        email=user_data.email,
        new_password=user_data.new_password
    )
    logic.provider.db.orm_dm3_5.delete_user_by_login(login=user.login)
    dataset = logic.provider.db.orm_dm3_5.get_user_by_login(login=user.login)
    assert len(dataset) == 0
    logic.provider.http.mailhog.delete_all_messages()
    return user


@pytest.fixture
def logic(set_config):
    return LogicProvider()
