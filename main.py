from typing import Union
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic 활용
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# Enum 활용을 통한 고정값 사용
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    # FastAPI는 타입힌트를 적극적으로 활용
    return {"item_id": item_id, "q" : q}

@app.put("/items/{item_id}")
async def read_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id" : item_id}

# users/me 와 users/{user_id} 가 연달아 나오는 경우 me 를 먼저 배치해야 충돌을 방지할 수 있음
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW! "}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images "}

    return {"model_name": model_name, "message": "Have some residuals "}

# file_path라는 매개변수는 경로와 일치하여야 함
@app.get("/files/{file_path:path}")
async def get_model(file_path: str):
    return {"file_path": file_path}