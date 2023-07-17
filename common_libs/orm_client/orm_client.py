import uuid
import structlog
from sqlalchemy import create_engine

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class OrmClient:
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        self.engine = create_engine(connection_string, isolation_level=isolation_level)
        self.db = self.engine.connect()
        self.log = structlog.getLogger(self.__class__.__name__).bind(service='DB')

    def close_connection(self):
        self.db.close()

    def send_query(self, query):
        print(query)
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=str(query),
        )
        # with self.db as connection:
        dataset = self.db.execute(statement=query)  # self.db - connection
        result = [row for row in dataset]
        log.msg(
            event='response',
            dataset=[dict(row) for row in result],
        )
        return result

    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=str(query),
        )
        self.db.execute(statement=query)
