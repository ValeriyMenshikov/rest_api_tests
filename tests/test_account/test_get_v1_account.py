def test_get_v1_account(dm_api_facade, prepare_user, orm_db, assertion):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    orm_db.delete_user_by_login(login=login)
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    assertion.check_user_was_created_for_prepare(login=login)
    dm_api_facade.account.activate_registered_user(login=login)
    assertion.check_user_was_activated(login=login)
    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.login.set_headers(headers=token)
    dm_api_facade.account.get_current_user()
    dm_api_facade.login.logout_user()
