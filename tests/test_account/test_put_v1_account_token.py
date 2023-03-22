import structlog
from services.dm_api_account import Facade
from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host='http://localhost:5051')
    response = api.account_api.put_v1_account_token(token='493efb5f-0ebb-46cf-9d7e-9e31ea447be8', status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "login_19",
            "roles": [UserRole.GUEST, UserRole.PLAYER]
        }
    ))
