from pydantic_settings import BaseSettings


class ProfileConfig(BaseSettings):
    db_pass: str
    db_user: str
    db_name: str
    db_host: str
    db_port: int = 5432

    @property
    def db_connection_url(self):
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

