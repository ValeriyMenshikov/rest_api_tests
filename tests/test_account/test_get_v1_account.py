def test_get_v1_account(logic, prepare_user, orm_db, assertion):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    logic.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    assertion.check_user_was_created_for_prepare(login=login)
    logic.account.activate_registered_user(login=login)
    assertion.check_user_was_activated(login=login)
    token = logic.login.get_auth_token(login=login, password=password)
    logic.set_headers(headers=token)
    logic.account.get_current_user()
    logic.login.logout_user()
