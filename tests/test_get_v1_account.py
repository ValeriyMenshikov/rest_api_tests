from services.dm_api_account import Facade


def test_get_v1_account():
    api = Facade(host='http://localhost:5051')
    api.account_api.get_v1_account()