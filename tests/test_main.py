from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main():
    r = client.get("/")
    assert r.status_code == status.HTTP_200_OK
