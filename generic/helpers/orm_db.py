from typing import List

import allure
from sqlalchemy import select, delete, update
from generic.helpers.orm_models import User
from common_libs.orm_client.orm_client import OrmClient


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.orm = OrmClient(user, password, host, database)

    def get_user_by_login(self, login) -> List[User]:
        with allure.step('Выбираем запись в БД по логину'):
            query = select([User]).where(User.Login == login)
        return self.orm.send_query(query=query)

    def get_all_users(self):
        with allure.step('Выбираем всю таблицу'):
            query = select([User])
        return self.orm.send_query(query=query)

    def delete_user_by_login(self, login):
        with allure.step('Удаляем пользователя из БД по логину'):
            query = delete(User).where(User.Login == login)
        return self.orm.send_bulk_query(query=query)

    def delete_user_by_email(self, email):
        with allure.step('Удаляем пользователя из БД по Email'):
            query = delete(User).where(User.Email == email)
        return self.orm.send_bulk_query(query=query)

    def activate_user_by_db(self, login):
        with allure.step('Активируем пользователя через БД'):
            query = update(User).values({User.Activated: True}).where(User.Login == login)
        return self.orm.send_bulk_query(query=query)

    def get_user_email(self):
        with allure.step('Выбор пользователя по email'):
            query = select([User.Email])
        return self.orm.send_query(query=query)
