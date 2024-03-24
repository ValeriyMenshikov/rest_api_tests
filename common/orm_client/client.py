import uuid

import structlog
from sqlalchemy import create_engine

from common.orm_client.singleton import SingletonMeta
from common.orm_client.utilities import allure_attach


class OrmClient(metaclass=SingletonMeta):
    def __init__(
        self,
        user,
        password,
        host,
        database,
        isolation_level="AUTOCOMMIT",
        disable_log=False,
    ):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        self.disable_log = disable_log
        self.engine = create_engine(connection_string, isolation_level=isolation_level)
        self.db = self.engine.connect()
        self.log = structlog.getLogger(self.__class__.__name__).bind(service="DB")

    def close_connection(self):
        self.db.close()

    @staticmethod
    def _compiled_query(query):
        query = query.compile(compile_kwargs={"literal_binds": True})
        return query

    @allure_attach
    def send_query(self, query):
        if self.disable_log:
            return [row for row in self.db.execute(statement=query)]
        query = self._compiled_query(query)
        print(query)  # noqa: T201
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event="request",
            query=str(query),
        )
        dataset = self.db.execute(statement=query)
        result = [row for row in dataset]
        log.msg(
            event="response",
            dataset=[dict(row) for row in result],
        )
        return result

    @allure_attach
    def send_bulk_query(self, query):
        if self.disable_log:
            return self.db.execute(statement=query)

        query = self._compiled_query(query)
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event="request",
            query=str(query),
        )
        self.db.execute(statement=query)
