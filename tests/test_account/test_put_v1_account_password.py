from modules.http.mailhog.mailhog import TokenType


def test_put_v1_account_password(logic, prepare_user, mailhog):
    login = prepare_user.login
    password = prepare_user.password
    new_password = prepare_user.new_password
    email = prepare_user.email

    logic.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    logic.account.activate_registered_user(login=login)
    token = logic.login.get_auth_token(login=login, password=password)
    logic.account.set_headers(headers=token)
    logic.account.reset_user_password(login=login, email=email)
    token = mailhog.get_token_by_login(login=login, token_type=TokenType.RESET_PASSWORD)
    logic.account.change_user_password(
        login=login,
        token=token,
        password=password,
        new_password=new_password
    )
