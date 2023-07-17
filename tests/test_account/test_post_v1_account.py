import allure
import pytest
import random
from string import ascii_letters, digits
from hamcrest import assert_that, has_entries


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    random_email = f'{random_string()}@{random_string()}.{random_string()}'
    valid_login = random_string(2)
    invalid_login = random_string(1, 1)
    valid_password = random_string(6)
    invalid_password = random_string(1, 5)
    invalid_email = f'{random_string(6)}@'
    invalid_email_1 = random_string(1, 2).replace('@', '')

    random_data = [
        (valid_login, random_email, valid_password, 201, ''),
        (valid_login, random_email, invalid_password, 400, {"Password": ["Short"]}),
        (invalid_login, random_email, valid_password, 400, {"Login": ["Short"]}),
        (valid_login, invalid_email, valid_password, 400, {"Email": ["Invalid"]}),
        (valid_login, invalid_email_1, valid_password, 400, {"Email": ["Invalid"]}),
    ]

    @pytest.mark.parametrize('login, email, password, status_code, check', random_data)
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            dm_db,
            login,
            email,
            password,
            assertion,
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
            assertion.check_user_was_created(login=login)
            dm_api_facade.account.activate_registered_user(login=login)
            assertion.check_user_was_activated(login=login)
            dm_api_facade.login.login_user(login=login, password=password)
        else:
            error_message = response.json()['errors']
            assert_that(error_message, has_entries(check))

    @allure.title("Проверка регистрации и активации пользователя")
    def test_register_and_activate_user(self, dm_api_facade, dm_db, prepare_user, assertion):
        """
        Тест проверяет создание и активацию пользователя в базе данных
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        dm_api_facade.account.register_new_user(login=login, email=email, password=password)
        assertion.check_user_was_created(login=login)
        dm_api_facade.account.activate_registered_user(login=login)
        assertion.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(login=login, password=password)


# В тестовые данные по желанию вставить нужных местах генерацию случайных строк
@pytest.mark.skip('tamplate')
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
