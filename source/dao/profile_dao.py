import logging
import psycopg2
from psycopg2.extras import RealDictCursor
from source.configuration.profile_db_config import ProfileConfig

logger = logging.getLogger(__name__)


class ProfileDao:
    def __init__(self, db_url: str):
        conf = ProfileConfig()
        self.db_url = conf.db_connection_url
        print("constructing connection url: ", db_url)

    def fetch_random_profile(self):
        print("💡 get_dao() called")
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM profiles LIMIT 1")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "description": row[2]}
        return None

    def get_profile_by_id(self, profile_id: int):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM profiles where id = %s", [profile_id])
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "description": row[2]}
        return None

    def insert_profile(self, name: str, description: str):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("INSERT INTO profiles (name, description) VALUES (%s, %s) RETURNING *", (name, description))
        inserted_profile = cur.fetchone()
        if not inserted_profile:
            conn.rollback()
            raise Exception("Insert failed: no row returned")
        conn.commit()
        cur.close()
        conn.close()
        return inserted_profile

