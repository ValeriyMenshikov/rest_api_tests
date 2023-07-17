def test_post_v1_account_password(dm_api_facade, prepare_user, assertion):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    assertion.check_user_was_created_for_prepare(login=login)
    dm_api_facade.account.activate_registered_user(login=login)
    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.account.reset_user_password(login=login, email=email)
