from fastapi import FastAPI, Response, Depends
from source.dao.profile_dao import ProfileDao
from source.models.profile import ProfileModel

app = FastAPI()


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
