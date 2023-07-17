import time


def test_put_v1_account_password(dm_api_facade, mailhog, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    new_password = prepare_user.new_password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
    )
    dm_api_facade.account.activate_registered_user(login=login)
    response = dm_api_facade.login.login_user(login=login, password=password)
    x_dm_auth_token = response[2]['X-Dm-Auth-Token']
    dm_api_facade.account.reset_user_password(login=login, email=email, x_dm_auth_token=x_dm_auth_token)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    dm_api_facade.account.change_user_password(
        login=login,
        token=token,
        old_password=password,
        new_password=new_password,
        x_dm_auth_token=x_dm_auth_token
    )
    dm_api_facade.login.login_user(login=login, password=new_password)
