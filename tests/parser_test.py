import os
from unittest.mock import AsyncMock

import pytest

from tests import assets
from tests.mocks import MockSession

os.environ["DATABASE_URL"] = "postgresql+psycopg://postgres:postgres@localhost:5432/app_db"
from parser.main import Parser



@pytest.mark.asyncio
async def test_process_pub_trade_msg(monkeypatch):
    p = Parser()
    msg = assets.test_msg

    mock_session = MockSession()

    monkeypatch.setattr("data.db.async_session", lambda: mock_session)

    await p.process_pub_trade_msg(msg)

    mock_session.add.assert_called_once()


