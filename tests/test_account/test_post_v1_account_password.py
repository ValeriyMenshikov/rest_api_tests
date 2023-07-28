def test_post_v1_account_password(logic, prepare_user, assertion):
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
    token = logic.login.get_auth_token(login=login, password=password)
    logic.account.set_headers(headers=token)
    logic.account.reset_user_password(login=login, email=email)
