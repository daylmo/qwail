import pytest
from fastapi import status
from fastapi.testclient import TestClient

from qwail.main import app

client = TestClient(app=app)


@pytest.mark.asyncio
async def test_main():
    r = client.get("/")
    assert r.status_code == status.HTTP_200_OK
