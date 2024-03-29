import asyncio

import pytest
from vyper import v
from grpclib.client import Channel

from modules.grpc.dm_api_account import AccountServiceStub, RegisterAccountRequest


@pytest.fixture
def event_loop() -> asyncio.AbstractEventLoop:
    """Create an instance of the default event loop for each test case."""
    yield asyncio.get_event_loop()


@pytest.fixture
def grpc_channel() -> Channel:
    """Initialize grpc channel."""
    return Channel(host=v.get("service.dm_api_account_grpc"), port=5055)


def pytest_sessionfinish(session: pytest.Session, exitstatus: int, grpc_channel: Channel) -> None:
    """Cleanup."""
    grpc_channel.close()
    asyncio.get_event_loop().close()


@pytest.fixture
def grpc_account(grpc_channel: Channel) -> AccountServiceStub:
    """Initialize grpc stub."""
    yield AccountServiceStub(channel=grpc_channel)


# https://stackoverflow.com/questions/61022713/pytest-asyncio-has-a-closed-event-loop-but-only-when-running-all-tests
@pytest.mark.asyncio
@pytest.mark.skip
async def test_register_account(grpc_account: AccountServiceStub) -> None:
    """Test register account."""
    response = await grpc_account.register_account(
        register_account_request=RegisterAccountRequest(
            login="login2029",
            email="login2029@email.ru",
            password="login_password",
        ),
    )

    assert response
