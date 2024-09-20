from pydantic import BaseModel


class EnterProduct(BaseModel):
    id: int
    quantity: int
