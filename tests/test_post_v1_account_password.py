from services.dm_api_account import DmApiAccount


def test_post_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "irure",
        "email": "nisi in"
    }
    api.account.post_v1_account_password(json=json)
