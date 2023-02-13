from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    response = api.account.put_v1_account_token(token='3c5371d8-2769-464f-abb2-82b5644de6e5')
    print(response)
    print(response['resource'])
    print(response['resource']['login'])
    print(response.resource.roles)

