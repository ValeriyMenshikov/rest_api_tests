from services.dm_api_account import Facade


def test_put_v1_account_email():
    api = Facade(host='http://localhost:5051')
    json = {
        "login": "ex adipisicing in pariatur ullamco",
        "password": "s",
        "email": "ut ut veniam Excepteur labore"
    }
    api.account_api.put_v1_account_email(json=json)
