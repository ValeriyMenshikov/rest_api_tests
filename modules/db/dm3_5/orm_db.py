from typing import List

import allure
from sqlalchemy import select, delete, update
from modules.db.dm3_5.orm_models import User
from common.orm_client import OrmClient


class OrmDatabase:
    def __init__(self, user: str, password: str, host: str, database: str, disable_log: bool = False) -> None:
        self.orm = OrmClient(user, password, host, database, disable_log=disable_log)

    def get_user_by_login(self, login) -> List[User]:
        with allure.step('Выбираем запись в БД по логину'):
            query = select(User).where(User.Login == login)
        return self.orm.send_query(query=query)

    def get_all_users(self) -> List[User]:
        with allure.step('Выбираем всю таблицу'):
            query = select(User)
        return self.orm.send_query(query=query)

    def delete_user_by_login(self, login: str) -> None:
        with allure.step('Удаляем пользователя из БД по логину'):
            query = delete(User).where(User.Login == login)
        return self.orm.send_bulk_query(query=query)

    def delete_user_by_email(self, email: str) -> None:
        with allure.step('Удаляем пользователя из БД по Email'):
            query = delete(User).where(User.Email == email)
        return self.orm.send_bulk_query(query=query)

    def activate_user_by_db(self, login: str) -> None:
        with allure.step('Активируем пользователя через БД'):
            query = update(User).values({User.Activated: True}).where(User.Login == login)
        return self.orm.send_bulk_query(query=query)

    def get_user_email(self) -> List[User]:
        with allure.step('Выбор пользователя по email'):
            query = select([User.Email])
        return self.orm.send_query(query=query)
