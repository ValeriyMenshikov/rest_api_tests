import allure
from hamcrest import assert_that, has_entries, has_properties


class AssertionsPostV1Account:
    def __init__(self, logic_provider):
        from generic import LogicProvider
        self.logic_provider: LogicProvider = logic_provider
        self.db = self.logic_provider.provider.db.dm3_5

    def check_user_was_created(self, login):
        with allure.step("Проверка что пользователь был создан"):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert_that(row, has_entries(
                    {
                        'Login': login,
                        'Activated': False
                    }
                ))

    def check_user_was_activated(self, login):
        with allure.step("Проверка что пользователь был активирован"):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert row['Activated'] is True, f'User {login} not activated'

    def check_user_was_created_for_prepare(self, login):
        with allure.step('check registered new user'):
            dataset = self.db.get_user_by_login(login=login)
            for row in dataset:
                assert_that(row, has_entries(
                    {
                        'Login': login,
                        'Activated': False
                    }
                ))
