def test_put_v1_account_token(dm_api_facade, prepare_user, assertion):
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
    assertion.check_user_was_activated(login=login)