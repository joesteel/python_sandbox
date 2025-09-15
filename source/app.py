from fastapi import FastAPI, Response, Depends, HTTPException
from source.dao.profile_dao import ProfileDao
from source.models.profile import ProfileModel
from source.models.InsertProfile import InsertProfileModel
import logging

app = FastAPI()
logging.basicConfig(
    level=logging.DEBUG,  # or INFO in production
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)


def get_dao():
    return ProfileDao("todo construct this properly from env data")


@app.get("/")
def read_root():
    headers = {"X-Custom-Header": "Connor Rocks"}
    return Response(content=
                    """
                     <html>
                     <head></head>
                     <body><h1>Hello, World!</h1></body>
                     </html>
                    """
                    , media_type="text/html", headers=headers)


@app.get("/random-profile", response_model=ProfileModel)
def get_random_profile(dao: ProfileDao = Depends(get_dao)):
    profile = dao.fetch_random_profile()
    return profile or {"error": "no profiles found"}


@app.get("/profiles/profile/{profile_id}", response_model=ProfileModel)
def get_random_profile(profile_id: int, dao: ProfileDao = Depends(get_dao)):
    profile = dao.get_profile_by_id(profile_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@app.post("/profiles", status_code=201, response_model=ProfileModel)
def create_profile(profile: InsertProfileModel, dao: ProfileDao = Depends(get_dao)):
    profile = dao.insert_profile(profile.name, profile.description)
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
