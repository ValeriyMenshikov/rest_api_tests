import time
import pytest
import random
from hamcrest import assert_that, has_entries
from collections import namedtuple
from string import ascii_letters, digits


@pytest.fixture
def prepare_user(dm_api_facade, dm_db):
    user = namedtuple('User', 'login, email, password')
    User = user(login="login_24", email="login_24@mail.ru", password="login_24")
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()

    return User


def test_post_v1_account(dm_api_facade, dm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': False
            }
        ))

    dm_api_facade.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

    dm_api_facade.login.login_user(
        login=login,
        password=password
    )


def random_string():
    symbols = ascii_letters + digits
    string = ''
    for _ in range(10):
        string += random.choice(symbols)
    return string


@pytest.mark.parametrize('login', [random_string() for _ in range(3)])
@pytest.mark.parametrize('email', [random_string() + '@' + random_string() + '.ru' for _ in range(3)])
@pytest.mark.parametrize('password', ['1', '2', '3'])
def test_post_v1_account_2(dm_api_facade, dm_db, login, email, password):
    dm_db.delete_user_by_login(login=login)
    dm_api_facade.mailhog.delete_all_messages()
    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row, has_entries(
            {
                'Login': login,
                'Activated': False
            }
        ))

    dm_api_facade.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

    dm_api_facade.login.login_user(
        login=login,
        password=password
    )
