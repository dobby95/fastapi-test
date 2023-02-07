from typing import Union, List
from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()


# Pydantic 활용
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# Enum 활용을 통한 고정값 사용
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


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

# fake_item_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     """
#     쿼리매개 변수
#     선택적으로 값을 가질 수 있고 기본값을 가질 수 있음
#     :param skip: 시작점
#     :param limit: 끝점
#     :return:
#     """
#     return fake_item_db[skip: skip + limit]
#
# @app.get("/items2/{item_id}")
# async def read_item2(item_id: str, q: Union[str, None] = None):
#     """
#     선택적 매개변수에 기본값을 None으로 설정
#     :param item_id:
#     :param q:
#     :return:
#     """
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}
#
# @app.get("/items3/{item_id}")
# async def read_item3(item_id: str, q: Union[str, None] = None, short: bool = False):
#     """
#     쿼리 매개 변수의 형변환, bool 타입의 경우 1, True, true, on, yes 변환 가능
#     :param item_id:
#     :param q:
#     :param short:
#     :return:
#     """
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
# ):
#     """
#     여러 경로의 매개변수와 쿼리 매개변수를 동시의 선언 가능
#     :param user_id:
#     :param item_id:
#     :param q:
#     :param short:
#     :return:
#     """
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
#
# @app.get("/items4/{item_id}")
# async def read_user_item2(item_id: str, needy: str):
#     """
#     매개변수에 기본값을 설정안할경우 그 값은 필수값이 됨
#     :param item_id:
#     :param needy:
#     :return:
#     """
#     item = {"item_id": item_id, "needy": needy}
#     return item
#
# @app.get("/items5/{item_id}")
# async def read_user_item3(
#     item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
# ):
#     """
#     일부는 필수로 다른 일부는 기본값을 넣어 선택적으로 활용 가능
#     :param item_id:
#     :param needy:
#     :param skip:
#     :param limit:
#     :return:
#     """
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item


################################################
################## 2023-02-05 ##################
################################################

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# @app.post("/items/")
# async def create_item(item: Item):
#     """
#     객체의 모든 속성에 직접 엑세스 가능
#     :param item:
#     :return:
#     """
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     """
#     경로매개변수와 Request Body를 함께 동시에 선언 가능
#     :param item_id:
#     :param item:
#     :return:
#     """
#     return {"item_id": item_id, **item.dict()}


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
#     """
#     Request Body, Path, Parameter 동시 선언 가능
#     :param item_id:
#     :param item:
#     :param q:
#     :return:
#     """
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def create_item(q: Union[str, None] = None):
#     """
#     매개변수에 대한 유효성 검사
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def read_item(q: Union[str, None] = Query(default=None, min_length=3, max_length=50)):
#     """
#     글자 길이 제한
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def read_item(q: Union[str, None] = Query(
#     default=None, min_length=3, max_length=50, regex="^fixedquery$"
# )):
#     """
#     정규식 정의
#     해당 정규식은 fixedquery로 시작하며 $뒤로는 글자가 오지못함 = fixedquery만 쓸 수 있음
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def read_item(q: Union[str, None] = Query(default=..., min_length=3)):
#     """
#     ... 은 해당값이 필수값임을 명시적으로 선언
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


from pydantic import Required


# @app.get("/items/")
# async def read_item(q: Union[str, None] = Query(default=Required, min_length=3)):
#     """
#     또는 Pydantic에서 Required로 표시
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def read_item(q: Union[List[str], None] = Query(default=None)):
#     """
#     매개변수 여러값을 동시 수신할 수 있음
#     :param q:
#     :return:
#     """
#     query_items = {"q": q}
#     return query_items


# @app.get("/items/")
# async def read_item(q: List[str] = Query(default=["foo", "bar"])):
#     """
#     list 매개변수에 대한 기본값 정의
#     :param q:
#     :return:
#     """
#     query_items = {"q": q}
#     return query_items

# @app.get("/items/")
# async def read_item(
#     q: Union[str, None] = Query(
#         default=None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     """
#     title 및 description
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/items/")
# async def read_item(
#     q: Union[str, None] = Query(
#         default=None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     """
#     title 및 description
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result

# @app.get("/items/")
# async def read_item(
#     q: Union[str, None] = Query(
#         default=None, alias="item-query"
#     )
# ):
#     """
#     alias를 동한 매개변수 찾기
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def read_item(
#     q: Union[str, None] = Query(
#         default=None,
#         alias="item-query",
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#         max_length=50,
#         regex="^fixedquery$",
#         deprecated=True,
#     )
# ):
#     """
#     매개변수 사용 중단(사용하는 클라이언트가 있고, 문서상 사용하지 않는것으로 표시 = deprecated
#     :param q:
#     :return:
#     """
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def read_item(
#     hidden_query: Union[str, None] = Query(default=None, include_in_schema=False)
# ):
#     """
#     자동문서시스템에서 쿼리매개변수를 제외하고 싶을 경우
#     :param q:
#     :return:
#     """
#     if hidden_query:
#         return {"hidden_qeury": hidden_query}
#     else:
#         return {"hidden_qeury": "Not Found"}
