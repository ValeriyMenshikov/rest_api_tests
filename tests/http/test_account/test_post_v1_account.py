import random
from string import digits, ascii_letters

import allure
import pytest
from hamcrest import assert_that, has_entries


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ""
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    random_email = f"{random_string()}@{random_string()}.{random_string()}"
    valid_login = random_string(2)
    invalid_login = random_string(1, 1)
    valid_password = random_string(6)
    invalid_password = random_string(1, 5)
    invalid_email = f"{random_string(6)}@"
    invalid_email_1 = random_string(1, 2).replace("@", "")

    random_data = [
        (valid_login, random_email, valid_password, 201, ""),
        (valid_login, random_email, invalid_password, 400, {"Password": ["Short"]}),
        (invalid_login, random_email, valid_password, 400, {"Login": ["Short"]}),
        (valid_login, invalid_email, valid_password, 400, {"Email": ["Invalid"]}),
        (valid_login, invalid_email_1, valid_password, 400, {"Email": ["Invalid"]}),
    ]

    @pytest.mark.parametrize("login, email, password, status_code, check", random_data)
    def test_create_and_activated_user_with_random_params(
        self,
        logic,
        login,
        email,
        password,
        status_code,
        check,
    ):
        logic.provider.db.orm_dm3_5.delete_user_by_login(login=login)
        logic.provider.http.mailhog.delete_all_messages()
        response = logic.account_helper.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code,
        )
        if status_code == 201:
            logic.assertions_helper.post_v1_account.check_user_was_created(login=login)
            logic.account_helper.activate_registered_user(login=login)
            logic.assertions_helper.post_v1_account.check_user_was_activated(
                login=login,
            )
            logic.login_helper.login_user(login=login, password=password)
        else:
            error_message = response.json()["errors"]
            assert_that(error_message, has_entries(check))

    @allure.title("Проверка регистрации и активации пользователя")
    def test_register_and_activate_user(self, logic, prepare_user):
        """
        Тест проверяет создание и активацию пользователя в базе данных
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        logic.account_helper.register_new_user(
            login=login,
            email=email,
            password=password,
        )
        logic.assertions_helper.post_v1_account.check_user_was_created(login=login)
        logic.account_helper.activate_registered_user(login=login)
        logic.assertions_helper.post_v1_account.check_user_was_activated(login=login)
        logic.login_helper.login_user(login=login, password=password)
