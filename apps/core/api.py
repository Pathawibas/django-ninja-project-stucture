# https://django-ninja.dev/guides/input/operations/
from typing import List
from ninja import Router
from apps.core.schema.hello_schema import HelloResponseSchema, HelloSchema, Error

router = Router()


@router.post("/hello", response={200: HelloResponseSchema, 403: Error})
def hello(request, data: HelloSchema):
    return {"message": f"Hello, POST {data.name}"}


@router.get("/hello/{int:hello_id}", response={200: HelloResponseSchema, 403: Error})
def retrieve_hello(request, hello_id: int):
    if hello_id == 1:
        return {"message": f"Hello, World! GET id:{hello_id}"}
    else:
        return {"message": "Forbidden"}, 403


@router.get("/hello")
def hello_world(request):
    return {"message": "Hello, World! GET"}


# list of objects
@router.get("/helloes", response=List[HelloResponseSchema])
def list_hello(request):
    hello_list = list(
        [{"message": "Hello, World! GET"}, {"message": "Hello, World! GET"}]
    )
    return hello_list
