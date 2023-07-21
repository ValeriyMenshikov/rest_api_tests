import uuid
import records
import structlog
from common_libs.db_client.utilities import allure_attach


class DbClient:
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        self.db = records.Database(connection_string, isolation_level=isolation_level)
        self.log = structlog.getLogger(self.__class__.__name__).bind(service='DB')

    @allure_attach
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

    @allure_attach
    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(evet_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query,
        )
        self.db.bulk_query(query=query)
