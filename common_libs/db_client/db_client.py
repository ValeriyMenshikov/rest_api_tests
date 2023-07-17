import uuid
import records
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class DbClient:
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        self.db = records.Database(connection_string, isolation_level=isolation_level)
        self.log = structlog.getLogger(self.__class__.__name__).bind(service='DB')

    def send_query(self, query):
        print(query)
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query,
        )
        dataset = self.db.query(query=query)
        log.msg(
            event='response',
            dataset=dataset,
        )
        return dataset.as_dict()

    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query,
        )
        self.db.bulk_query(query=query)
