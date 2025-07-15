import logging

import psycopg2
from source.configuration.profile_db_config import ProfileConfig


class ProfileDao:
    def __init__(self, db_url: str):
        conf = ProfileConfig()
        self.db_url = conf.db_connection_url
        logging.log(1, "constructing connection url: ", db_url)


    def fetch_random_profile(self):
        conn = psycopg2.connect(self.db_url)
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM profiles LIMIT 1")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return {"id": row[0], "name": row[1], "description": row[2]}
        return None
