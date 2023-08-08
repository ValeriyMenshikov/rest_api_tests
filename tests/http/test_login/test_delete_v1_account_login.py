def test_del_v1_account_login(logic, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    logic.account_helper.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    logic.account_helper.activate_registered_user(login=login)
    token = logic.login_helper.get_auth_token(login=login, password=password)
    logic.login_helper.logout_user(headers=token)