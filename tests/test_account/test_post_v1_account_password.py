def test_post_v1_account_password(dm_api_facade, prepare_user, assertion):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
    )
    assertion.check_user_was_created_for_prepare(login=login)
    dm_api_facade.account.activate_registered_user(login=login)
    response = dm_api_facade.login.login_user(login=login, password=password)
    x_dm_auth_token = response[2]['X-Dm-Auth-Token']
    dm_api_facade.account.reset_user_password(login=login, email=email, x_dm_auth_token=x_dm_auth_token)
