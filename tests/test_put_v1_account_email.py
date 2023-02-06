from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "ex adipisicing in pariatur ullamco",
        "password": "s",
        "email": "ut ut veniam Excepteur labore"
    }
    api.account.put_v1_account_email(json=json)
