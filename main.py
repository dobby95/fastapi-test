from typing import Union

from fastapi import FastAPI, Body, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = None,
    item: Union[Item, None] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item, user: User):
    """
    여러개의 Body Parameter 도 가능
    :param item_id:
    :param item:
    :param user:
    :return:
    """
    results = {"item_id": item_id, "item": item, "user": user}
    return results


@app.put("/items3/{item_id}")
async def update_item3(item_id: int, item: Item, user: User, importance: int = Body()):
    """
    query와 path 와 같이 추가 데이터에 대해 받는것을 Body를 통해 받을 수 있음. 단 싱글 밸류임
    :param item_id:
    :param item:
    :param user:
    :param importance:
    :return:
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.put("/items4/{item_id}")
async def update_item4(
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(gt=0),
        q: Union[str, None] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results



@app.put("/items5/{item_id}")
async def update_item5(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

