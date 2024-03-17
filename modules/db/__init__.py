from functools import cached_property
from modules.db.dm3_5.orm_db import OrmDatabase
from modules.db.dm3_5.dm_db import DmDatabase
from vyper import v


class DBConnector:
    @cached_property
    def orm_dm3_5(self) -> OrmDatabase:
        return OrmDatabase(
            user=v.get("database.dm3_5.user"),
            password=v.get("database.dm3_5.password"),
            database=v.get("database.dm3_5.database"),
            host=v.get("database.dm3_5.host"),
            disable_log=v.get("disable_log"),
        )

    @cached_property
    def dm3_5(self) -> DmDatabase:
        return DmDatabase(
            user=v.get("database.dm3_5.user"),
            password=v.get("database.dm3_5.password"),
            database=v.get("database.dm3_5.database"),
            host=v.get("database.dm3_5.host"),
            disable_log=v.get("disable_log"),
        )
