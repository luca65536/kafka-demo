from pydantic import BaseModel


class Item(BaseModel):
    """
        Basic item dummy model.
    """
    item_id: int
    description: str = None
