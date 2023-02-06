from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    api.account.put_v1_account_token(token='123123213')
