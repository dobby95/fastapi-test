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

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     # FastAPI는 타입힌트를 적극적으로 활용
#     return {"item_id": item_id, "q" : q}
#
# @app.put("/items/{item_id}")
# async def read_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id" : item_id}
#
# # users/me 와 users/{user_id} 가 연달아 나오는 경우 me 를 먼저 배치해야 충돌을 방지할 수 있음
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}
#
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW! "}
#
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images "}
#
#     return {"model_name": model_name, "message": "Have some residuals "}
#
# # file_path라는 매개변수는 경로와 일치하여야 함
# @app.get("/files/{file_path:path}")
# async def get_model(file_path: str):
#     return {"file_path": file_path}

################################################
################## 2023-02-01 ##################
################################################

fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    쿼리매개 변수
    선택적으로 값을 가질 수 있고 기본값을 가질 수 있음
    :param skip: 시작점
    :param limit: 끝점
    :return:
    """
    return fake_item_db[skip: skip + limit]

@app.get("/items2/{item_id}")
async def read_item2(item_id: str, q: Union[str, None] = None):
    """
    선택적 매개변수에 기본값을 None으로 설정
    :param item_id:
    :param q:
    :return:
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/items3/{item_id}")
async def read_item3(item_id: str, q: Union[str, None] = None, short: bool = False):
    """
    쿼리 매개 변수의 형변환, bool 타입의 경우 1, True, true, on, yes 변환 가능
    :param item_id:
    :param q:
    :param short:
    :return:
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    """
    여러 경로의 매개변수와 쿼리 매개변수를 동시의 선언 가능
    :param user_id:
    :param item_id:
    :param q:
    :param short:
    :return:
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items4/{item_id}")
async def read_user_item2(item_id: str, needy: str):
    """
    매개변수에 기본값을 설정안할경우 그 값은 필수값이 됨
    :param item_id:
    :param needy:
    :return:
    """
    item = {"item_id": item_id, "needy": needy}
    return item

@app.get("/items5/{item_id}")
async def read_user_item3(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    """
    일부는 필수로 다른 일부는 기본값을 넣어 선택적으로 활용 가능
    :param item_id:
    :param needy:
    :param skip:
    :param limit:
    :return:
    """
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item