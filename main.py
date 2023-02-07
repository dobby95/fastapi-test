from typing import Union

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: Union[str, None] = Query(default=None, alias = "item-query")
):
    """
    메타데이터 선언.
    Query에 동일한 매개변수를 선언할 수 있음
    :param item_id:
    :param q:
    :return:
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


@app.get("/items2/{item_id}")
async def read_items2(q: str, item_id: int = Path(title="The ID of the item to get")):
    """
    기본값이 없는 q를 뒤에 둘 경우 Error 발생 --> 이를 방지하기 위해선 순서를 바꿔줘야함
    FastAPI에서 매개변수 순서가 중요하지 않음
    :param item_id:
    :param q:
    :return:
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


@app.get("/items3/{item_id}")
async def read_items3(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    """
    * 는 아무런 행동도 하지 않음. 다만, * 추가를 통해 기본값이 없는 q가 정상적으로 작동 할 수 잇음
    :param item_id:
    :param q:
    :return:
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


@app.get("/items4/{item_id}")
async def read_items4(*, item_id: int = Path(title="The ID of the item to get", ge=1), q: str):
    """
    숫자 검증. ge = greater and equal
    :param item_id:
    :param q:
    :return:
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


@app.get("/items5/{item_id}")
async def read_items5(*, item_id: int = Path(title="The ID of the item to get", gt=0, le=1000), q: str):
    """
    숫자 검증. gt = greater then, le = less equal
    :param item_id:
    :param q:
    :return:
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results


@app.get("/items6/{item_id}")
async def read_items6(
        *,
        item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
        q: str,
        size: float = Query(gt=0, lt=10.5)
):
    """
    숫자 검증.
    :param item_id:
    :param q:
    :return:
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results