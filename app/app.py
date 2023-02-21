from fastapi import FastAPI
from starlette import status

from app.model import HelloModel

app = FastAPI()


@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=HelloModel,
)
def read_root():
    return HelloModel(message="Hello World")
