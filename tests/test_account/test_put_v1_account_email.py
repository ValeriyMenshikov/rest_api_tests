def test_put_v1_account_email(dm_api_facade, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    dm_api_facade.account.activate_registered_user(login=login)
    dm_api_facade.account.change_user_email(login=login, password=password, email=email)
