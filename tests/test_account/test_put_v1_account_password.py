from modules.http.mailhog.client import TokenType


def test_put_v1_account_password(logic, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    new_password = prepare_user.new_password
    email = prepare_user.email

    logic.account_helper.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    logic.account_helper.activate_registered_user(login=login)
    access_token = logic.login_helper.get_auth_token(login=login, password=password)
    logic.account_helper.reset_user_password(login=login, email=email, headers=access_token)
    reset_token = logic.provider.http.mailhog.get_token_by_login(login=login, token_type=TokenType.RESET_PASSWORD)
    logic.account_helper.change_user_password(
        login=login,
        token=reset_token,
        password=password,
        new_password=new_password,
        headers=access_token
    )
