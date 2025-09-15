from fastapi.testclient import TestClient
from source.app import app, get_dao

fake_id = 42
fake_name = "stubbed name"
fake_description = "stubbed description"
fake_profile_json = {"id": fake_id, "name": fake_name, "description": fake_description}


class StubProfileDAO:
    last_inserted = {}

    def fetch_random_profile(self):
        return fake_profile_json

    def get_profile_by_id(self, profile_id: int):
        return fake_profile_json

    def insert_profile(self, name: str, description: str):
        fake_inserted_profile = {
            "id": fake_id,
            "name": name,
            "description": description
        }
        self.last_inserted = fake_inserted_profile
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


def test_profile_by_id():
    app.dependency_overrides[get_dao] = lambda: StubProfileDAO()

    client = TestClient(app)
    response = client.get("/profiles/profile/1")
    assert response.status_code == 200
    assert response.json() == fake_profile_json

    app.dependency_overrides = {}
    return None


def test_insert_profile():
    stub_dao = StubProfileDAO()
    app.dependency_overrides[get_dao] = lambda: stub_dao

    client = TestClient(app)
    payload = {"name": fake_name, "description": fake_description}

    response = client.post('/profiles/', json=payload)
    expected_profile = {
            "id": fake_id,
            "name": fake_name,
            "description": fake_description
        }
    assert response.json() == expected_profile
    assert stub_dao.last_inserted == expected_profile
    return None
