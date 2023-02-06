from services.dm_api_account import DmApiAccount


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "commodo",
        "password": "veniam do dolor",
        "rememberMe": False
    }
    api.login.post_v1_account_login(json=json)
