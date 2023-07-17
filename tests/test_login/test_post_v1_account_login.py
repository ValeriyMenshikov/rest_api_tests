def test_post_v1_account_login(dm_api_facade, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
    )
    dm_api_facade.account.activate_registered_user(login=login)
    dm_api_facade.login.login_user(login=login, password=password)
