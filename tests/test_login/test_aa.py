from generic.helpers.orm_db import OrmDatabase


def test_db():
    OrmDatabase(host='localhost', database='dm3.5', user='postgres', password='admin').get_all_users()
    # dm_db.get_all_users()