from fastapi.testclient import TestClient
from source.app import app, get_dao

fake_profile_json = {"id": 42, "name": "Stub", "description": "Fake profile"}


class StubProfileDAO:
    def fetch_random_profile(self):
        return fake_profile_json


def test_root_custom_header():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers.get("X-Custom-Header") == "Connor Rocks"
    return None


def test_random_profile():
    app.dependency_overrides[get_dao] = lambda: StubProfileDAO()

    client = TestClient(app)
    response = client.get("/random-profile")
    assert response.status_code == 200
    assert response.json() == fake_profile_json

    app.dependency_overrides = {}
    return None
