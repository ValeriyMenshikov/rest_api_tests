def test_put_v1_account_email(logic, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    logic.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    logic.account.activate_registered_user(login=login)
    logic.account.change_user_email(login=login, password=password, email=email)
