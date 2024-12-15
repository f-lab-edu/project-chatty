import uvicorn
from fastapi import FastAPI

from apis import route_chat


def include_router(app: FastAPI):
    app.include_router(route_chat.router)


def start_application():
    _app = FastAPI()
    include_router(_app)
    return _app


app = start_application()

if __name__ == "__main__":
    uvicorn.run("src:main:app", host="0.0.0.0", port=8000, reload=True)
