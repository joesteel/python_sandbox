from fastapi.testclient import TestClient
from source.app import app

client = TestClient(app)


def test_root_custom_header():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers.get("X-Custom-Header") == "Connor Rocks"
