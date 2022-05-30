from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware


class MyPostData(BaseModel):
    name: str
    mean: str


app = FastAPI()

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    data: str
    ningen: str
    id: int

class basic(BaseModel):
    name: str
    value: float

# テスト用辞書
test_data = {
    "pachinko": "玉を弾く遊び",
    "slot": "リールを回す遊び",
}

@app.get("/")
async def index():
    return {"message": "hello world"}


@app.get("/data/")
def read_data_max(key: str):

    print(key)
    print(test_data[key])
    return test_data[key]


# @app.post("/data/")
# def update_data(post_data: MyPostData):
#     test_data[post_data.name] = post_data.mean
#     return {"message": "post success!!"}

@app.post("/data/")
def update_data(post_data: MyPostData):
    test_data[post_data.name] = post_data.mean
    return {
        "mess1": None,
        "mess2": "tsuchida2",
        "data": "flaja"
    }


@app.get("/datasaikou/")
def tsuchida_data(tsuchida: str):
    return tsuchida