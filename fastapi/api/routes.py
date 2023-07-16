from fastapi import APIRouter
from .models import Item

router = APIRouter()


@router.get("/", description="Yggrasil.", tags=["Dev-only"])
def read_root():
    """
        Root route.

        This endpoint will greet you once you have setted up our project.
    """
    return {"Hello": "World"}


@router.get("/items/{item_id}", description="This endpoint allows you to \
    retrieve an item based on its ID. The `item_id` path parameter should be \
    provided.", tags=["Dev-only"], summary="Retrieve an item")
def read_item(item_id: int):
    """
        Retrieve item by ID.

        This endpoint allows you to retrieve an item based on its ID.
        The `item_id` path parameter should be provided.
    """
    item = Item(item_id=item_id, description='This a sample description.')
    return item.dict()
