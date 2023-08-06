def test_put_v1_account_token(logic, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email

    logic.account_helper.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )

    logic.assertions_helper.post_v1_account.check_user_was_created_for_prepare(login=login)
    logic.account_helper.activate_registered_user(login=login)
    logic.assertions_helper.post_v1_account.check_user_was_activated(login=login)
