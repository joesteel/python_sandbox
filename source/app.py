from fastapi import FastAPI, Response

app = FastAPI()


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
