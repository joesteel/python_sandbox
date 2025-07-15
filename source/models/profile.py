from pydantic import BaseModel


class ProfileModel(BaseModel):
    id: int
    name: str
    description: str
