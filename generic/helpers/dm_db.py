import allure

from db_client.db_client import DbClient


class DmDatabase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        query = 'select * from "public"."Users"'
        with allure.step('Выбираем всю таблицу'):
            return self.db.send_query(query=query)

    def get_user_by_login(self, login):
        query = f'''
        select * from "public"."Users" where "Login" = '{login}'
        '''
        with allure.step('Выбираем запись в БД по логину'):
            return self.db.send_query(query=query)

    def delete_user_by_login(self, login):
        query = f'''
        delete from "public"."Users"
        where "Login" = '{login}'
        '''
        with allure.step('Удаляем пользователя из БД по логину'):
            return self.db.send_bulk_query(query=query)

    def activate_user_by_db(self, login):
        query = f'''
        update "public"."Users"
        set "Activated" = true
        where "Login" = '{login}'
        '''
        with allure.step('Активируем пользователя через БД'):
            return self.db.send_bulk_query(query=query)
