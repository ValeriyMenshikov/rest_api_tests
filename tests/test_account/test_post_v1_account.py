import allure
import pytest
import random
from collections import namedtuple
from string import ascii_letters, digits

from hamcrest import assert_that, has_entries

from data.post_v1_account import PostV1AccountData as user_data


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    @pytest.mark.parametrize('login, email, password, status_code, check', [
        (random_string(2), f'{random_string()}@{random_string()}.{random_string()}', random_string(6), 201, ''),
        (random_string(2), f'{random_string()}@{random_string()}.{random_string()}', random_string(1, 5), 400, {"Password": ["Short"]}),
        (random_string(1, 1), f'{random_string()}@{random_string()}.{random_string()}', random_string(6), 400, {"Login": ["Short"]}),
        (random_string(2), f'{random_string(6)}@', random_string(6), 400, {"Email": ["Invalid"]}),
        (random_string(2), random_string(1, 2), random_string(6), 400, {"Email": ["Invalid"]}),
    ])
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            dm_db,
            login,
            email,
            password,
            assertions,
            status_code,
            check
    ):
        dm_db.delete_user_by_login(login=login)
        dm_api_facade.mailhog.delete_all_messages()
        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        if status_code == 201:
            assertions.check_user_was_created(login=login)
            dm_api_facade.account.activate_registered_user(login=login)
            assertions.check_user_was_activated(login=login)
            dm_api_facade.login.login_user(login=login, password=password)
        else:
            error_message = response.json()['errors']
            assert_that(error_message, has_entries(check))

    @allure.step("Подготовка тестового пользователя")
    @pytest.fixture
    def prepare_user(self, dm_api_facade, dm_db):
        user = namedtuple('User', 'login, email, password')
        User = user(login=user_data.login, email=user_data.email, password=user_data.password)
        dm_db.delete_user_by_login(login=User.login)
        dataset = dm_db.get_user_by_login(login=User.login)
        assert len(dataset) == 0
        dm_api_facade.mailhog.delete_all_messages()

        return User

    @allure.title("Проверка регистрации и активации пользователя")
    def test_register_and_activate_user(self, dm_api_facade, dm_db, prepare_user, assertions):
        """
        Тест проверяет создание и активацию пользователя в базе данных
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        dm_api_facade.account.register_new_user(login=login, email=email, password=password)
        assertions.check_user_was_created(login=login)
        dm_api_facade.account.activate_registered_user(login=login)
        assertions.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(login=login, password=password)


# В тестовые данные по желанию вставить нужных местах генерацию случайных строк
@pytest.mark.parametrize('login, email, password, status_code, check', [
    ('12', '12@12.ru', '123456', 201, ''),  # Валидные данные
    ('12', '12@12.ru', random_string(1, 5), 400, {"Password": ["Short"]}),  # Пароль менее либо равен 5 символам
    ('1', '12@12.ru', '123456', 400, {"Login": ["Short"]}),  # Логин менее 2 символов
    ('12', '12@', '123456', 400, {"Email": ["Invalid"]}),  # Емейл не содержит доменную часть
    ('12', '12', '123456', 400, {"Email": ["Invalid"]}),  # Емейл не содержит символ @
])
def test_create_and_activated_user_with_random_params(
        dm_api_facade,
        dm_db,
        login,
        email,
        password,
        assertions,
        status_code,
        check
):
    dm_db.delete_user_by_login(login=login)
    dm_api_facade.mailhog.delete_all_messages()
    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    if status_code == 201:
        # Активация пользователя
        # Блок проверки в базе данных и логин пользователя
        ...
    else:
        # Реализовать блок проверки соответствия сообщения возвращаемого в response сообщению "check"
        ...
