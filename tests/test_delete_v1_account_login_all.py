from services.dm_api_account import Facade


def test_delete_v1_account_login_all():
    api = Facade(host='http://localhost:5051')
    api.login_api.delete_v1_account_login_all()