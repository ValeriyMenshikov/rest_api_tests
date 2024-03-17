def test_post_v1_account_password(logic, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    logic.account_helper.register_new_user(
        login=login, email=email, password=password, status_code=201
    )
    logic.assertions_helper.post_v1_account.check_user_was_created_for_prepare(
        login=login
    )
    logic.account_helper.activate_registered_user(login=login)
    token = logic.login_helper.get_auth_token(login=login, password=password)
    logic.account_helper.reset_user_password(login=login, email=email, headers=token)
