import time


def test_put_v1_account_password(dm_api_facade, prepare_user, mailhog):
    login = prepare_user.login
    password = prepare_user.password
    new_password = prepare_user.new_password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    dm_api_facade.account.activate_registered_user(login=login)
    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.account.reset_user_password(login=login, email=email)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    dm_api_facade.account.change_user_password(
        login=login,
        token=token,
        password=password,
        new_password=new_password
    )
