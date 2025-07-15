from source.configuration.profile_db_config import ProfileConfig
import os


def test_db_connection_url():
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_USER"] = "aiuser"
    os.environ["DB_NAME"] = "profiledb"
    os.environ["DB_PORT"] = "5432"
    os.environ["DB_PASS"] = "pass123"

    pc = ProfileConfig()
    assert pc.db_connection_url == "postgresql://aiuser:pass123@localhost:5432/profiledb"

    del os.environ["DB_HOST"]
    del os.environ["DB_USER"]
    del os.environ["DB_NAME"]
    del os.environ["DB_PORT"]
    del os.environ["DB_PASS"]
