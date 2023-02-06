from services.dm_api_account import DmApiAccount


def test_get_v1_account():
    api = DmApiAccount(host='http://localhost:5051')
    api.account.get_v1_account()