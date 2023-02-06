from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "occaecat reprehenderit in laborum",
        "token": "84060d01-09e6-096e-2459-1409207d00c7",
        "oldPassword": "est",
        "newPassword": "do aliquip "
    }
    api.account.put_v1_account_password(json=json)
