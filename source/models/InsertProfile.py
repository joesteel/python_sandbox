from pydantic import BaseModel


class InsertProfileModel(BaseModel):
    name: str
    description: str
