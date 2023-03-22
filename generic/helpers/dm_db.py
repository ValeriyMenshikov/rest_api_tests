from common_libs.db_client.db_client import DbClient


class DmDatabase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        query = 'select * from "public"."Users"'
        dataset = self.db.send_query(query=query)
        return dataset

    def get_user_by_login(self, login):
        query = f'''
        select * from "public"."Users"
        where "Login" = '{login}'
        '''
        dataset = self.db.send_query(query=query)
        return dataset

    def delete_user_by_login(self, login):
        query = f'''
        delete from "public"."Users" 
        where "Login" = '{login}'
        '''
        dataset = self.db.send_bulk_query(query=query)
        return dataset
