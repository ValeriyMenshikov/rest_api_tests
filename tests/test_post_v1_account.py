import allure
import pytest
import random
from collections import namedtuple
from string import ascii_letters, digits


def random_string():
    symbols = ascii_letters + digits
    string = ''
    for _ in range(10):
        string += random.choice(symbols)
    return string


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:

    @allure.step("Подготовка тестового пользователя")
    @pytest.fixture
    def prepare_user(self, dm_api_facade, dm_db):
        user = namedtuple('User', 'login, email, password')
        User = user(login="login_24", email="login_24@mail.ru", password="login_24")
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

    @pytest.mark.parametrize('login', [random_string() for _ in range(3)])
    @pytest.mark.parametrize('email', [random_string() + '@' + random_string() + '.ru' for _ in range(3)])
    @pytest.mark.parametrize('password', ['1', '2', '3'])
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            dm_db,
            login,
            email,
            password,
            assertions
    ):
        dm_db.delete_user_by_login(login=login)
        dm_api_facade.mailhog.delete_all_messages()
        dm_api_facade.account.register_new_user(login=login, email=email, password=password)
        assertions.check_user_was_created(login=login)
        dm_api_facade.account.activate_registered_user(login=login)
        assertions.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(login=login, password=password)
