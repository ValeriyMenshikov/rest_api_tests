import requests


def delete_v1_account_login():
    """
    Logout as current user
    :return:
    """
    url = "http://localhost:5051/v1/account/login"

    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="DELETE",
        url=url,
        headers=headers
    )
    return response
