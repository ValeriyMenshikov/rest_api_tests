from collections import namedtuple
import grpc
import pytest
import structlog
from vyper import v
from pathlib import Path
from generic.assertions.post_v1_account import AssertionsPostV1Account
from generic.helpers.dm_db import DmDatabase
from generic.helpers.mailhog import MailhogApi
from generic.helpers.orm_db import OrmDatabase
from generic.helpers.search import Search
from services.dm_api_account import Facade
# from apis.dm_api_search_async import SearchEngineStub
from grpclib.client import Channel
from data.post_v1_account import PostV1AccountData as user_data

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def grpc_search():
    client = Search(target=v.get('service.dm_api_search'))
    yield client
    client.grpc_search.close()


@pytest.fixture
def grpc_search_async():
    channel = Channel(host='localhost', port=5052)
    client = SearchEngineStub(channel)
    yield client
    channel.close()


options = (
    'service.dm_api_account',
    'service.mailhog',
    'database.dm3_5.host'
)


@pytest.fixture
def prepare_user(dm_api_facade, orm_db):
    user_tuple = namedtuple('User', 'login, email, password, new_password')
    user = user_tuple(
        login=user_data.login,
        password=user_data.password,
        email=user_data.email,
        new_password=user_data.new_password
    )
    orm_db.delete_user_by_login(login=user.login)
    dataset = orm_db.get_user_by_login(login=user.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()
    return user


@pytest.fixture
def mailhog():
    return MailhogApi(host=v.get('service.mailhog'))


@pytest.fixture
def dm_api_facade(mailhog):
    return Facade(host=v.get('service.dm_api_account'),
                  mailhog=mailhog
                  )


@pytest.fixture
def orm_db(request):
    orm = OrmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        database=v.get('database.dm3_5.database'),
        host=v.get('database.dm3_5.host')
    )

    def fin():
        orm.orm.close_connection()

    request.addfinalizer(fin)
    return orm


# connections = None


# @pytest.fixture(scope='session')
# def orm_db():
#     global connections
#     if connections is None:
#         connections = OrmDatabase(
#             user=v.get('database.dm3_5.user'),
#             password=v.get('database.dm3_5.password'),
#             database=v.get('database.dm3_5.database'),
#             host=v.get('database.dm3_5.host')
#         )
#     yield connections
#     connections.orm.close_connection()


@pytest.fixture
def dm_db(request):
    connect = DmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        database=v.get('database.dm3_5.database'),
        host=v.get('database.dm3_5.host')
    )

    def fin():
        connect.db.db.close()

    request.addfinalizer(fin)

    return connect


@pytest.fixture
def assertion(orm_db):
    return AssertionsPostV1Account(orm_db)


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
